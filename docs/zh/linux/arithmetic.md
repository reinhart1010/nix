---
layout: page
title: linux/arithmetic (中文)
description: "测试见到你的算术问题。"
content_hash: 97a41cc98530ee63749fa341ea6525e8252f5f9f
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/linux/arithmetic.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arithmetic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# arithmetic

测试见到你的算术问题。
更多信息：<https://manpages.debian.org/latest/bsdgames/arithmetic.6.en.html>.

- 开始算术测试：

`arithmetic`

- 指定一个或多个算术运算符来设计问题：

`arithmetic -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-|x|/</span>

- 指定范围。加法和乘法问题限定 0 到指定范围之间的数字，包含上区间。减法和除法问题限制结果和运算数字必须在 0 到指定范围之间：

`arithmetic -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
