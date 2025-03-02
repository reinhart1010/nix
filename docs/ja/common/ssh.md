---
layout: page
title: common/ssh (日本語)
description: "Secure Shell は、リモートシステムに安全にログオンするために使用されるプロトコルです。"
content_hash: 6da1412ed40a210549ab0bad1211808328a896c8
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ssh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ssh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh

Secure Shell は、リモートシステムに安全にログオンするために使用されるプロトコルです。
これは、リモート・サーバー上でのロギングやコマンド実行に使用できます。
もっと詳しく: <https://man.openbsd.org/ssh>。

- リモートサーバに接続する:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>

- 特定のID(秘密鍵)でリモートサーバに接続する:

`ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/key_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>

- 特定のポート([p]ort)を使ってリモートサーバに接続する:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2222</span>

- リモートコマンドとのやり取りを許可する[t]ty割当を使って、リモートサーバ上でコマンドを実行する:

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド引数</span>

- SSHトンネリング： [D]ynamic port forwarding (`localhost:1080` の SOCKSプロキシ):

`ssh -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>

- SSHトンネリング： 特定のポート(`localhost:9999`から`example.org:80`)を転送し、擬似[T]tyの割当とリモートコマンドの実行(executio[N])を無効にする:

`ssh -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -N -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>

- SSH [J]umping： ジャンプホストを経由して、リモートサーバーに接続する (カンマ区切りで複数のジャンプホップを指定できる):

`ssh -J `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ジャンプホスト</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ユーザ名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">リモートホスト</span>

- ハングしたセッションを閉じる:

`<Enter> ~ .`
