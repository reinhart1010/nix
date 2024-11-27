---
layout: page
title: common/bc (中文)
description: "任意精度的计算器语言。"
content_hash: 7a729b19181b860b526c70c3cc6291d8ac3e5be6
last_modified_at: 2024-11-27
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
  - title: 日本語 version
    url: /ja/common/bc.html
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
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bc

任意精度的计算器语言。
请参阅：`dc`，`qalc`。
更多信息：<https://manned.org/bc>.

- 启动交互式会话：

`bc`

- 启动交互式会话并启用标准数学库：

`bc --interactive --mathlib`

- 计算表达式：

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- 执行脚本：

`bc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.bc</span>

- 使用指定的小数位数计算一个表达式：

`echo 'scale = `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`; `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5 / 3</span>`' | bc`

- 使用 `mathlib` 计算正弦/余弦/反正切/自然对数/指数函数：

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s|c|a|l|e</span>`(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`)' | bc --mathlib`

- 执行一个内联的阶乘脚本：

`echo "define factorial(n) { if (n <= 1) return 1; return n*factorial(n-1); }; factorial(`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>`)" | bc`
