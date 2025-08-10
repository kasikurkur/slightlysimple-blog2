# slightlysimple.net DNS設定手順

## 概要
独自ドメイン `slightlysimple.net` をGitHub Pagesで使用するためのDNS設定手順です。

## 1. 必要なDNSレコード

### Aレコード（必須）
ドメインのルート（slightlysimple.net）をGitHub PagesのIPアドレスに向けます。

```
ホスト名: @ (または slightlysimple.net)
レコードタイプ: A
値: 185.199.108.153

ホスト名: @ (または slightlysimple.net)
レコードタイプ: A
値: 185.199.109.153

ホスト名: @ (または slightlysimple.net)
レコードタイプ: A
値: 185.199.110.153

ホスト名: @ (または slightlysimple.net)
レコードタイプ: A
値: 185.199.111.153
```

### CNAMEレコード（推奨）
wwwサブドメインをGitHub Pagesに向けます。

```
ホスト名: www
レコードタイプ: CNAME
値: kasikurkur.github.io
```

## 2. 主要ドメインレジストラでの設定方法

### お名前.com
1. ドメイン管理画面にログイン
2. 「DNS設定」→「DNSレコード設定」
3. 上記のAレコードとCNAMEレコードを追加
4. 設定を保存

### ムームードメイン
1. ムームードメイン管理画面にログイン
2. 「ドメイン管理」→「ムームーDNS」
3. 「変更」ボタンをクリック
4. 上記のレコードを追加
5. 「セットアップ情報変更」をクリック

### Cloudflare
1. Cloudflareダッシュボードにログイン
2. slightlysimple.net ドメインを選択
3. 「DNS」タブを選択
4. 「レコードを追加」で上記のレコードを設定
5. プロキシ状況は「DNS only」（灰色クラウド）に設定

### Route 53 (AWS)
1. AWS Route 53コンソールにアクセス
2. Hosted zoneでslightlysimple.netを選択
3. 「Create record」で上記のレコードを作成

## 3. DNS設定確認方法

### コマンドラインでの確認
```bash
# Aレコードの確認
dig slightlysimple.net A

# CNAMEレコードの確認
dig www.slightlysimple.net CNAME

# nslookupでの確認
nslookup slightlysimple.net
nslookup www.slightlysimple.net
```

### オンラインツールでの確認
- [DNS Checker](https://dnschecker.org/)
- [What's My DNS](https://whatsmydns.net/)
- [DNS Propagation Checker](https://www.whatsmydns.net/)

## 4. GitHub Pages設定

DNS設定完了後、GitHub Pages側の設定を行います。

1. https://github.com/kasikurkur/slightlysimple-blog2/settings/pages にアクセス
2. Custom domain欄に `slightlysimple.net` を入力
3. 「Save」をクリック
4. DNS設定が反映されるまで待機（数分〜24時間）
5. 「Enforce HTTPS」をチェック（証明書発行後）

## 5. 設定完了確認

### 1. サイトアクセス確認
- https://slightlysimple.net でサイトが表示される
- https://www.slightlysimple.net でもサイトが表示される
- HTTPSでアクセスできる（証明書発行完了後）

### 2. リダイレクト確認
- www.slightlysimple.net → slightlysimple.net へのリダイレクト
- HTTP → HTTPS へのリダイレクト

## 6. トラブルシューティング

### よくある問題

#### DNS設定が反映されない
- **原因**: DNS伝播には時間がかかります
- **対処法**: 24-48時間待機してから再確認

#### SSL証明書エラー
- **原因**: DNS設定が不完全、またはまだ伝播中
- **対処法**: DNS設定を再確認し、数時間後に「Enforce HTTPS」を再試行

#### サイトが404エラー
- **原因**: GitHub PagesのCustom domain設定が正しくない
- **対処法**: GitHub Pages設定でドメイン名を再入力

#### CNAMEファイルが消える
- **原因**: GitHub Pages設定時に自動生成されるはず
- **対処法**: `static/CNAME` ファイルの存在確認（既に作成済み）

### 確認コマンド例

```bash
# DNS伝播状況確認
dig +short slightlysimple.net
# 結果例: 185.199.108.153 などGitHub PagesのIPが返される

# HTTPS証明書確認
curl -I https://slightlysimple.net
# 結果例: HTTP/2 200 などHTTPSで正常応答

# サイトの内容確認
curl -s https://slightlysimple.net | grep -i title
# 結果例: ページタイトルが表示される
```

## 7. 設定完了後の運用

### 定期確認項目
- [ ] サイトが正常にアクセスできる
- [ ] HTTPS証明書が有効期限内
- [ ] DNS設定が変更されていない

### 年次作業
- [ ] ドメイン更新
- [ ] DNS設定の見直し

---

**設定完了目安時間**: DNS設定 10分、伝播待ち 24-48時間  
**最終更新**: 2025-08-10  
**作成者**: Claude Code