# これなに

ひなビタ♪ Facebook ページの投稿を蒐集するやつ

# 環境

Linux 前提

# 使い方

- <https://developers.facebook.com> でアプリを作成し，アプリ ID と app secret を取得して，それぞれ `conf.json` の `app_id` と `app_secret` に書き込んでください。
- 作成したアプリの設定画面の，プロダクト → Facebook ログインの項から，有効な OAuth リダイレクト URI の欄に次を入力してください

> http://localhost:8000/cgi-bin/get_token

- 次に以下のコマンドを入力してください

```
$ ./startup.sh
$ ./get_token.sh
```

- ブラウザで <http://localhost:8000/cgi-bin/index> にアクセスして表示されているリンクを踏む
- Facebook にログインしてアクセスを許可する
- 元のページに戻って `user_access` というキーがある json が表示されていればアクセストークン取得に成功
- `token.json` が作成されているか確認
- ./get_token.sh を停止する

- 最後にこのコマンド

```
$ ./run.sh
```

これで，`hinabitter.txt` というテキストファイルが得られます。
`hinabitter.txt` は青空文庫形式のテキストです。

