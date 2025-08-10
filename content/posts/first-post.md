---
title: "WindowsでSSH鍵を簡単に生成する方法"
date: 2025-08-10T09:49:57+09:00
draft: false
tags: ["Windows", "SSH", "セキュリティ", "GitHub"]
categories: ["技術tips"]
description: "WindowsでSSH鍵を簡単に生成してGitHubに設定する手順を分かりやすく説明します"
---

## はじめに

「slightlysimple」へようこそ！このブログでは、日常で役立つ技術的なtipsを分かりやすく説明していきます。

今回は、Windows環境でSSH鍵を生成してGitHubに設定する方法をご紹介します。パスワード入力なしでGitHubにアクセスできるようになり、開発作業が格段に楽になります。

## SSH鍵とは？

SSH鍵は、パスワードの代わりに使用する認証方式です。秘密鍵と公開鍵のペアを作成し、公開鍵をGitHubに登録することで安全な接続が可能になります。

## 手順1: SSH鍵の生成

### Windows PowerShellを開く
1. `Windows + R` キーを押す
2. `powershell` と入力してEnter

### SSH鍵を生成
```bash
ssh-keygen -t rsa -b 4096 -C "your.email@example.com"
```

- `-t rsa`: RSA暗号化方式を使用
- `-b 4096`: 4096ビットの鍵長（セキュリティ強化）
- `-C`: コメント（メールアドレスを記載）

## 手順2: 生成された鍵の確認

```bash
# 公開鍵の内容を表示
Get-Content ~/.ssh/id_rsa.pub
```

この内容をコピーします。

## 手順3: GitHubに公開鍵を登録

1. [GitHub](https://github.com) にログイン
2. 右上のプロフィール → Settings
3. SSH and GPG keys → New SSH key
4. Title に分かりやすい名前を入力
5. Key に先ほどコピーした公開鍵を貼り付け
6. Add SSH key をクリック

## 手順4: 接続テスト

```bash
ssh -T git@github.com
```

「Hi [ユーザー名]! You've successfully authenticated...」と表示されれば成功です。

## まとめ

SSH鍵の設定は一度行えば、今後のGitHub操作が大幅に楽になります。セキュリティも向上するので、ぜひ設定してみてください。

今後も日常で使える技術的なtipsを紹介していきますので、お楽しみに！
