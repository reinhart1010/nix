---
layout: page
title: linux/whatis (日本語)
description: "マニュアルページから、一行の説明文を表示します。"
content_hash: 9a0de721dac24c2b03b53ff255942fb4d66546b8
last_modified_at: 2023-01-16
related_topics:
  - title: English version
    url: /en/linux/whatis.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/whatis.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># whatis

マニュアルページから、一行の説明文を表示します。
詳しくはこちら: <https://manned.org/whatis>.

- manページの説明文を表示する:

`whatis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- 説明文を行末で切らないで表示する:

`whatis --long `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>

- globパターンにマッチするすべてのコマンドの説明文を表示する:

`whatis --wildcard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">net*</span>

- 正規表現でmanページの説明文を検索する:

`whatis --regex '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wish[0-9]\.[0-9]</span>`'`

- 言語を指定して説明文で表示する (`manpage-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ja</span> パッケージが必要です):

`whatis --locale=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ja</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>