---
layout: page
title: common/case (日本語)
description: "複数の選択肢がある条件文を作成するための Bash 組み込み構文。"
content_hash: b294866ec9b7170c5c0aa5424c0f06f9d1899a3d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/case.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/case.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/case.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/case.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/case.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># case

複数の選択肢がある条件文を作成するための Bash 組み込み構文。
もっと詳しく: <https://www.gnu.org/software/bash/manual/bash.html#index-case>。

- 変数を文字列リテラルとマッチさせ、実行するコマンドを決める:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$tocount</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">words</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lines</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>`; ;; esac`

- パターンは | で結合し、どれにも該当しないパターンには \* を使う:

`case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$tocount</span>` in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[wW]|words</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -w README</span>`; ;; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[lL]|lines</span>`) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wc -l README</span>`; ;; *) `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "what?"</span>`; ;; esac`
