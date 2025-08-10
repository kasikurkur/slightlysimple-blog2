#!/usr/bin/env python3
"""
記事品質向上スクリプト
Claude APIを使用して記事のSEO最適化と文章改善を行う
"""

import os
import sys
import yaml
import re
import argparse
from pathlib import Path
from datetime import datetime

def read_markdown_file(file_path):
    """Markdownファイルを読み込み、フロントマターと本文を分離"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # フロントマター分離
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            body = parts[2].strip()
            return frontmatter, body
    
    # フロントマターがない場合
    return {}, content

def write_markdown_file(file_path, frontmatter, body):
    """フロントマターと本文をMarkdownファイルに書き込み"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n\n')
        f.write(body)

def extract_keywords_from_content(content):
    """コンテンツからキーワードを抽出（簡易版）"""
    # 日本語の単語を抽出（ひらがな、カタカナ、漢字、英数字）
    words = re.findall(r'[ぁ-んァ-ヶ一-龯a-zA-Z0-9]+', content)
    
    # よく使われる単語を除外
    stop_words = {'こと', 'もの', 'ため', 'など', 'について', 'による', 'ます', 'です', 'である', 'する', 'れる', 'られる'}
    
    # 長い単語を優先してキーワードとして抽出
    keywords = [word for word in words if len(word) >= 3 and word not in stop_words]
    
    # 重複削除して最初の10個を返す
    return list(dict.fromkeys(keywords))[:10]

def generate_meta_description(title, content):
    """タイトルと内容から自動でメタディスクリプションを生成"""
    # 最初の段落から160文字程度を抽出
    first_paragraph = content.split('\n\n')[0]
    # マークダウン記法を除去
    clean_text = re.sub(r'[#*`\[\]()]', '', first_paragraph)
    # 改行を除去
    clean_text = re.sub(r'\n+', ' ', clean_text).strip()
    
    if len(clean_text) > 160:
        clean_text = clean_text[:157] + '...'
    
    return clean_text

def suggest_tags_from_content(content):
    """内容から関連タグを提案"""
    # 技術系キーワードのマッピング
    tech_keywords = {
        'ChatGPT': ['ChatGPT', 'AI', '人工知能'],
        'AI': ['AI', '人工知能', '機械学習'],
        'プログラミング': ['プログラミング', '開発', 'コード'],
        'ブログ': ['ブログ', 'ブログ運営', 'コンテンツ'],
        'SEO': ['SEO', '検索エンジン', 'マーケティング'],
        'Python': ['Python', 'プログラミング', '開発'],
        'JavaScript': ['JavaScript', 'Web開発', 'プログラミング'],
    }
    
    suggested_tags = set()
    content_lower = content.lower()
    
    for keyword, tags in tech_keywords.items():
        if keyword.lower() in content_lower:
            suggested_tags.update(tags)
    
    return list(suggested_tags)[:5]  # 最大5個まで

def enhance_frontmatter(frontmatter, content, file_path):
    """フロントマターを強化"""
    enhanced = frontmatter.copy()
    
    # タイトルがない場合はファイル名から生成
    if 'title' not in enhanced:
        enhanced['title'] = Path(file_path).stem.replace('-', ' ').title()
    
    # 日付がない場合は現在の日付を設定
    if 'date' not in enhanced:
        enhanced['date'] = datetime.now().isoformat()
    
    # draft設定がない場合はfalseに設定
    if 'draft' not in enhanced:
        enhanced['draft'] = False
    
    # メタディスクリプションがない場合は自動生成
    if 'description' not in enhanced:
        enhanced['description'] = generate_meta_description(enhanced.get('title', ''), content)
    
    # タグがない場合は自動提案
    if 'tags' not in enhanced:
        enhanced['tags'] = suggest_tags_from_content(content)
    
    # カテゴリがない場合はタグから推定
    if 'categories' not in enhanced and enhanced.get('tags'):
        enhanced['categories'] = [enhanced['tags'][0]]  # 最初のタグをカテゴリに
    
    return enhanced

def main():
    parser = argparse.ArgumentParser(description='記事品質向上スクリプト')
    parser.add_argument('file_path', help='処理するMarkdownファイルのパス')
    parser.add_argument('--output', help='出力ファイルパス（指定しない場合は元ファイルを上書き）')
    parser.add_argument('--dry-run', action='store_true', help='実際の変更は行わず、提案のみ表示')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"エラー: ファイル '{args.file_path}' が見つかりません")
        sys.exit(1)
    
    # Markdownファイル読み込み
    frontmatter, content = read_markdown_file(args.file_path)
    
    print(f"処理中: {args.file_path}")
    print("=" * 50)
    
    # フロントマター強化
    enhanced_frontmatter = enhance_frontmatter(frontmatter, content, args.file_path)
    
    # 変更点の表示
    print("【フロントマター変更点】")
    for key, value in enhanced_frontmatter.items():
        if key not in frontmatter:
            print(f"  追加: {key} = {value}")
        elif frontmatter[key] != value:
            print(f"  変更: {key} = {frontmatter[key]} → {value}")
    
    # キーワード抽出結果表示
    keywords = extract_keywords_from_content(content)
    print(f"\n【抽出キーワード】")
    print(f"  {', '.join(keywords[:5])}")
    
    # dry-runでない場合は実際に保存
    if not args.dry_run:
        output_path = args.output or args.file_path
        write_markdown_file(output_path, enhanced_frontmatter, content)
        print(f"\n✅ ファイルを更新しました: {output_path}")
    else:
        print(f"\n🔍 Dry-runモード: 実際の変更は行われていません")

if __name__ == "__main__":
    main()