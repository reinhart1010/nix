---
layout: page
title: windows/net (日本語)
description: "ネットワーク関連の設定を表示、変更するためのシステムユーティリティ。"
content_hash: 5891906d3c2c4bbbb241cc50e9ffb922ec94e0b5
last_modified_at: 2025-03-02
related_topics:
  - title: বাংলা version
    url: /bn/windows/net.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/net.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/windows/net.html
    icon: bi bi-globe
tldri18n_status: 2
---
# net

ネットワーク関連の設定を表示、変更するためのシステムユーティリティ。
もっと詳しく: <https://learn.microsoft.com/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/gg651155(v=ws.11)>。

- Windowsサービスを同期的に開始または停止する:

`net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">start|stop</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サービス</span>

- 現在のコンソールでSMB共有が利用可能であることを確認する:

`net use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\smb共有フォルダ</span>` /USER:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>

- 現在SMBで共有されているフォルダを表示する:

`net share`

- SMB共有の使用者を表示する(管理者特権コンソールで実行):

`net session`

- ローカルセキュリティグループ内のユーザーを表示する:

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`"`

- ローカルセキュリティグループにユーザーを追加する(管理者特権コンソールで実行):

`net localgroup "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Administrators</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>` /add`

- サブコマンドのヘルプを表示する:

`net help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">サブコマンド</span>

- ヘルプを表示する:

`net help`
