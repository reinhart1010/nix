---
layout: page
title: linux/sed (日本語)
description: "スクリプタブルな方法でテキストを編集します。"
content_hash: 21e4d705d5928a2c413187edb065c7bef4f5e465
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sed.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/sed.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sed.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sed

スクリプタブルな方法でテキストを編集します。
`awk`, `ed` も参照してください。
もっと詳しく: <https://www.gnu.org/software/sed/manual/sed.html>。

- 全ての入力行の `apple` (基本正規表現)を `mango` (基本正規表現)に置換し、結果を`stdout`に出力する:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed 's/apple/mango/g'`

- 全ての入力行で出現する全ての `apple` (拡張正規表現)を `APPLE` (拡張正規表現)に置換し、結果を`stdout`に出力する:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -E 's/(apple)/\U\1/g'`

- 特定のファイルに出現する全ての `apple` (基本正規表現)を `mango` (基本正規表現)に置換し、元のファイルを上書きする:

`sed -i 's/apple/mango/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- 特定のスクリプトファイル([f]ile)を実行し、結果を`stdout`に出力する:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/script.sed</span>

- 最初の行だけを`stdout`に出力する:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` | sed -n '1p'`

- ファイルの最初の行を削除([d]elete)する:

`sed -i 1d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- ファイルの先頭行に改行を挿入([i]nsert)する:

`sed -i '1i\your new line text\' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>
