---
layout: page
title: common/sed (日本語)
description: "スクリプトによるテキスト編集。"
content_hash: fb0ccca7c84d990d2e7301b24ce645e23b098598
last_modified_at: 2024-06-13
related_topics:
  - title: dansk version
    url: /da/common/sed.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sed.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sed.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sed

スクリプトによるテキスト編集。
詳しくはこちら: <https://manned.org/sed.1posix>

- ファイルの各行で正規表現の最初の出現箇所を置換し、その結果を表示する:

`sed 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正規表現</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>

- ファイル内の拡張正規表現のすべての出現箇所を置換し、その結果を表示する:

`sed -r 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">正規表現</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>

- ファイル内のすべての文字列を置き換え、ファイルを上書きする(すなわち インプレイス):

`sed -i 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え前</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名}</span>

- ラインパターンに一致する行のみを置換:

`sed '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ラインパターン</span>`/s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え前</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>

- ラインパターンに一致する行を削除する:

`sed '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ラインパターン</span>`/d' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名}</span>

- ファイルの最初の 11 行を表示する:

`sed 11q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>

- 複数の検索・置換式をファイルに適用:

`sed -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え名</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/' -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え前</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>

- 区切り文字 `/` を、検索や置換のパターンで使われていない他の文字（例：`#`）で置き換える:

`sed 's#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え前</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">置き換え後</span>`#' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ファイル名</span>
