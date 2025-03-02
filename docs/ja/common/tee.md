---
layout: page
title: common/tee (日本語)
description: "`stdin` から読み込んで `stdout` とファイル(またはコマンド)に書き込みます。"
content_hash: 88042dc87e6fba84a0ce1cf127bd4b4c91135a96
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/tee.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tee.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tee.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/tee.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tee

`stdin` から読み込んで `stdout` とファイル(またはコマンド)に書き込みます。
もっと詳しく: <https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html>。

- 各ファイルに `stdin` をコピーし、`stdout` にもコピーする:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 与えられたファイルに追記する。上書きはしない:

`echo "example" | tee -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- ターミナルに `stdin` を表示し、さらに処理するために別のプログラムにパイプする:

`echo "example" | tee `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/tty</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">xargs printf "[%s]"</span>

- "example"と言うディレクトリを作成し、"example"の文字バイト数を数え、"example"をターミナルに出力する:

`echo "example" | tee >(xargs mkdir) >(wc -c)`
