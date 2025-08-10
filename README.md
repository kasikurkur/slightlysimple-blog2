# ChatGPT調査結果ブログ

ChatGPTを活用した調査結果をまとめるブログサイトです。Hugo + GitHub Pages + AdSenseによる収益化システムを構築しています。

## 🚀 特徴

- **静的サイトジェネレーター**: Hugo + PaperMod テーマ
- **ホスティング**: GitHub Pages（完全無料）
- **自動デプロイ**: GitHub Actions
- **収益化**: Google AdSense
- **分析**: Google Analytics 4
- **SEO最適化**: サイトマップ、robots.txt、メタタグ自動生成
- **記事品質向上**: Python スクリプトによる自動最適化

## 📁 ディレクトリ構成

```
blog-site/
├── content/posts/          # 記事用Markdownファイル
├── static/                 # 静的ファイル（画像、CSS等）
├── layouts/partials/       # AdSense用レイアウト
├── scripts/                # 記事品質向上スクリプト
├── .github/workflows/      # GitHub Actions設定
├── config.yaml            # Hugo設定
└── 運用マニュアル.md        # 詳細な運用手順
```

## 🛠️ セットアップ手順

### 1. 前提条件
- Git がインストールされていること
- Hugo extended版 がインストールされていること
- GitHub アカウントを持っていること

### 2. リポジトリクローン
```bash
git clone https://github.com/ユーザー名/blog-site.git
cd blog-site
git submodule update --init --recursive
```

### 3. ローカル開発
```bash
# 開発サーバー起動
hugo server -D

# ブラウザで http://localhost:1313 を確認
```

### 4. 記事作成
```bash
# 新記事作成
hugo new content posts/記事タイトル.md

# 記事品質向上（オプション）
python3 scripts/simple-enhance.py content/posts/記事タイトル.md --dry-run
```

## 🎯 運用フロー

1. **記事作成**: `content/posts/` に Markdown ファイルを作成
2. **品質向上**: Python スクリプトでSEO最適化
3. **プレビュー**: `hugo server` でローカル確認
4. **公開**: Git push で自動デプロイ

詳細は [運用マニュアル.md](./運用マニュアル.md) を参照してください。

## 💰 収益化設定

### Google AdSense
1. AdSense アカウント作成・申請
2. 承認後、`config.yaml` の AdSense 設定を更新
3. `adsense.enabled: true` に変更

### Google Analytics
1. GA4 プロパティ作成
2. `config.yaml` の `googleAnalytics` を更新

## 📊 コスト

- **ホスティング**: 無料（GitHub Pages）
- **ドメイン**: 年間約1,000円（独自ドメイン使用時）
- **合計**: 年間1,000円以下

## 🔧 技術スタック

- **Hugo**: v0.148.2 (Extended)
- **テーマ**: PaperMod
- **CI/CD**: GitHub Actions
- **言語**: Go (Hugo), Python (スクリプト)

## 📈 パフォーマンス

- **ページ読み込み**: 3秒以内
- **Core Web Vitals**: 最適化済み
- **SEO**: 構造化データ、サイトマップ対応
- **レスポンシブ**: モバイル完全対応

## 🛠️ トラブルシューティング

よくある問題と解決策：

### Hugo build エラー
```bash
hugo --verbose  # 詳細なエラー確認
```

### サブモジュール更新
```bash
git submodule update --recursive --remote
```

### GitHub Actions 失敗
Actions タブでログを確認し、Hugo バージョンや設定を見直してください。

## 📚 参考資料

- [Hugo 公式ドキュメント](https://gohugo.io/documentation/)
- [PaperMod テーマ](https://github.com/adityatelange/hugo-PaperMod)
- [GitHub Pages ドキュメント](https://docs.github.com/pages)

## 📝 ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。

---

**🤖 Generated with [Claude Code](https://claude.ai/code)**

**Co-Authored-By: Claude <noreply@anthropic.com>**