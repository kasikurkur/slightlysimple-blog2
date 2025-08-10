#!/usr/bin/env python3
"""
簡易記事品質向上スクリプト（PyYAMLなし版）
"""

import os
import sys
import re
import argparse
from pathlib import Path
from datetime import datetime

def read_markdown_file(file_path):
    """Markdownファイルを読み込み、フロントマターと本文を分離"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # YAML フロントマター分離（簡易版）
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_text = parts[1].strip()
            body = parts[2].strip()
            return frontmatter_text, body
    
    return '', content

def parse_yaml_simple(yaml_text):
    """簡易YAML解析（基本的なkey: value形式のみ）"""
    result = {}
    for line in yaml_text.split('\n'):
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip().strip('"\'')
            
            # リスト形式の処理
            if value.startswith('[') and value.endswith(']'):
                # 簡易リスト解析
                items = value[1:-1].split(',')
                result[key] = [item.strip().strip('"\'') for item in items]
            else:
                result[key] = value
    
    return result

def generate_yaml_simple(data):
    """簡易YAML生成"""
    lines = []
    for key, value in data.items():
        if isinstance(value, list):
            formatted_list = '[' + ', '.join(f'"{item}"' for item in value) + ']'
            lines.append(f'{key}: {formatted_list}')
        else:
            lines.append(f'{key}: "{value}"')
    
    return '\n'.join(lines)

def extract_keywords_from_content(content):
    """コンテンツからキーワードを抽出"""
    # 日本語の単語を抽出
    words = re.findall(r'[ぁ-んァ-ヶ一-龯a-zA-Z0-9]+', content)
    
    # よく使われる単語を除外
    stop_words = {'こと', 'もの', 'ため', 'など', 'について', 'による', 'ます', 'です', 'である', 'する', 'れる', 'られる'}
    
    # 長い単語を優先
    keywords = [word for word in words if len(word) >= 3 and word not in stop_words]
    
    return list(dict.fromkeys(keywords))[:10]

def generate_meta_description(title, content):
    """メタディスクリプション生成"""
    first_paragraph = content.split('\n\n')[0]
    clean_text = re.sub(r'[#*`\[\]()]', '', first_paragraph)
    clean_text = re.sub(r'\n+', ' ', clean_text).strip()
    
    if len(clean_text) > 160:
        clean_text = clean_text[:157] + '...'
    
    return clean_text

def suggest_tags_from_content(content):
    """内容から関連タグを提案"""
    tech_keywords = {
        'ChatGPT': ['ChatGPT', 'AI', '人工知能'],
        'AI': ['AI', '人工知能', '機械学習'],
        'プログラミング': ['プログラミング', '開発', 'コード'],
        'ブログ': ['ブログ', 'ブログ運営', 'コンテンツ'],
        'SEO': ['SEO', '検索エンジン', 'マーケティング'],
    }
    
    suggested_tags = set()
    content_lower = content.lower()
    
    for keyword, tags in tech_keywords.items():
        if keyword.lower() in content_lower:
            suggested_tags.update(tags)
    
    return list(suggested_tags)[:5]

def main():
    parser = argparse.ArgumentParser(description='簡易記事品質向上スクリプト')
    parser.add_argument('file_path', help='処理するMarkdownファイルのパス')
    parser.add_argument('--dry-run', action='store_true', help='実際の変更は行わず、提案のみ表示')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file_path):
        print(f"エラー: ファイル '{args.file_path}' が見つかりません")
        sys.exit(1)
    
    # Markdownファイル読み込み
    frontmatter_text, content = read_markdown_file(args.file_path)
    frontmatter = parse_yaml_simple(frontmatter_text)
    
    print(f"処理中: {args.file_path}")
    print("=" * 50)
    
    # 改善提案
    suggestions = {}
    
    if 'description' not in frontmatter or not frontmatter.get('description'):
        title = frontmatter.get('title', Path(args.file_path).stem.replace('-', ' ').title())
        suggestions['description'] = generate_meta_description(title, content)
    
    if 'tags' not in frontmatter or not frontmatter.get('tags'):
        suggestions['tags'] = suggest_tags_from_content(content)
    
    # キーワード抽出
    keywords = extract_keywords_from_content(content)
    
    print("【改善提案】")
    for key, value in suggestions.items():
        print(f"  {key}: {value}")
    
    print(f"\n【抽出キーワード】")
    print(f"  {', '.join(keywords[:5])}")
    
    if not args.dry_run and suggestions:
        # フロントマター更新
        updated_frontmatter = frontmatter.copy()
        updated_frontmatter.update(suggestions)
        
        # ファイル保存
        with open(args.file_path, 'w', encoding='utf-8') as f:
            f.write('---\n')
            f.write(generate_yaml_simple(updated_frontmatter))
            f.write('\n---\n\n')
            f.write(content)
        
        print(f"\n✅ ファイルを更新しました: {args.file_path}")
    else:
        print(f"\n🔍 Dry-runモードまたは更新なし")

if __name__ == "__main__":
    main()