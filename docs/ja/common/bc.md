---
layout: page
title: common/bc (日本語)
description: "任意の精度で計算を行える言語です。"
content_hash: b164a8b491917f3a414bf5e27089a4ef40064bb9
last_modified_at: 2023-09-20
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

任意の精度で計算を行える言語です。
`dc`も参照してください。
詳しくはこちら: <https://manned.org/man/bc.1>.

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
