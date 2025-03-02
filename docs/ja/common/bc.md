---
layout: page
title: common/bc (日本語)
description: "任意の精度で計算を行える言語です。"
content_hash: 677a57fb4baae244f2dd3ab83b7b46e199b1335c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/bc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/bc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bc.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/bc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/bc.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

任意の精度で計算を行える言語です。
`dc`も参照してください。
もっと詳しく: <https://manned.org/bc>。

- 対話モードのセッションを開始する:

`bc`

- 標準数学ライブラリを有効化して対話モードのセッションを開始する:

`bc --mathlib`

- 式を計算する:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- スクリプトを実行する:

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">スクリプト/への/パス.bc</span>

- 小数点以下の桁数を指定して式を計算する:

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- `mathlib`を使用してサイン/コサイン/アークタンジェント/自然対数/指数関数を計算する:

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`
