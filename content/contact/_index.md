---
title: "お問い合わせ"
description: "slightlysimpleへのお問い合わせページ"
showDate: false
showAuthor: false
showReadingTime: false
showEdit: false
---

# お問い合わせ

**slightlysimple** に関するご質問、ご提案、その他お問い合わせは、以下の方法でお気軽にご連絡ください。

---

## 📧 お問い合わせフォーム

以下のフォームをご利用いただくか、直接メールでお問い合わせください。

<div class="contact-form">

**お名前**：  
<input type="text" id="name" name="name" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ddd; border-radius: 4px;">

**メールアドレス**：  
<input type="email" id="email" name="email" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ddd; border-radius: 4px;">

**お問い合わせカテゴリ**：  
<select id="category" name="category" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ddd; border-radius: 4px;">
  <option value="">カテゴリを選択してください</option>
  <option value="記事内容">記事内容について</option>
  <option value="技術的質問">技術的な質問</option>
  <option value="サイト不具合">サイトの不具合報告</option>
  <option value="取材・コラボ">取材・コラボレーションについて</option>
  <option value="その他">その他</option>
</select>

**お問い合わせ内容**：  
<textarea id="message" name="message" rows="6" style="width: 100%; padding: 8px; margin: 8px 0; border: 1px solid #ddd; border-radius: 4px;" placeholder="できるだけ具体的にご記入ください"></textarea>

<button type="button" onclick="sendEmail()" style="background-color: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin-top: 10px;">
  📤 送信する
</button>

</div>

<script>
function sendEmail() {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const category = document.getElementById('category').value;
    const message = document.getElementById('message').value;
    
    if (!name || !email || !message) {
        alert('必須項目を入力してください');
        return;
    }
    
    const subject = `[slightlysimple] ${category || 'お問い合わせ'}`;
    const body = `お名前: ${name}\n` +
                 `メールアドレス: ${email}\n` +
                 `カテゴリ: ${category}\n\n` +
                 `お問い合わせ内容:\n${message}\n\n` +
                 `---\n` +
                 `送信日時: ${new Date().toLocaleString('ja-JP')}`;
    
    const mailtoLink = `mailto:contact@slightlysimple.net?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.location.href = mailtoLink;
}
</script>

---

## 📮 直接メール

**メールアドレス**: contact@slightlysimple.net

お問い合わせの際は、以下の情報をご記入いただけると、より適切なご回答が可能です：

- お名前（ハンドルネーム可）
- お問い合わせのカテゴリ
- 具体的なご質問・ご要望

---

## ⏰ 返信について

### 返信時間の目安
- **平日**: 3営業日以内
- **土日祝日**: 5営業日以内

### 返信が遅れる場合
以下の場合、返信にお時間をいただく場合があります：
- 技術的な調査が必要な場合
- 長期休暇期間中
- お問い合わせ内容が複雑な場合

---

## 📝 お問い合わせ内容について

### よくあるお問い合わせ

#### **記事内容について**
- 記事の内容に関するご質問
- より詳しい説明のリクエスト
- 記事の訂正・更新要求

#### **技術的質問**
- 記事で紹介したツールの使い方
- 設定方法の詳細
- トラブルシューティング

#### **サイトの不具合**
- ページが表示されない
- リンクが機能しない
- モバイル表示の問題

#### **取材・コラボレーション**
- インタビュー取材
- 商品レビュー依頼
- コラボレーション企画

### ⚠️ お問い合わせ時の注意事項

1. **個人情報について**
   - 必要最小限の情報のみご記入ください
   - クレジットカード番号等の機密情報は記載しないでください

2. **返信について**
   - 迷惑メールフォルダもご確認ください
   - ドメイン受信設定で「@slightlysimple.net」を許可してください

3. **商用利用について**
   - 商用目的のお問い合わせも歓迎します
   - 内容によってはお断りする場合があります

---

## 🔒 プライバシーについて

お問い合わせでいただいた個人情報は、[プライバシーポリシー](/privacy/)に従って適切に管理いたします。

- **利用目的**: お問い合わせへの対応のみ
- **保存期間**: 対応完了から1年間
- **第三者提供**: 法的要求がある場合を除き行いません

---

## 🤝 その他のご連絡方法

### GitHub
技術的な問題やサイトの改善提案は、GitHubでもお受けしています：  
[https://github.com/kasikurkur](https://github.com/kasikurkur)

### ソーシャルメディア
※準備中

---

**運営チーム**: slightlysimple  
**お問い合わせ対応時間**: 平日 9:00-18:00  
**最終更新**: 2025年8月10日