---
layout: page
title: common/qalc (中文)
description: "强大且易用的命令行计算器。"
content_hash: 8412d28424e32df665685cf1027f8ebdf5619586
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qalc.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/qalc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qalc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qalc

强大且易用的命令行计算器。
请参阅：`bc`。
更多信息：<https://qalculate.github.io/manual/qalc.html>.

- 以交互模式启动：

`qalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--interactive</span>

- 以简洁模式启动（仅输出结果）：

`qalc --terse`

- 更新货币兑换率：

`qalc --exrates`

- 非交互地执行计算：

`qalc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">66+99|2^4|6 feet to cm|1 bitcoin to USD|20 kmph to mph|...</span>

- 列出所有支持的函数/前缀/单位/变量：

`qalc --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">list-functions|list-prefixes|list-units|list-variables</span>

- 从文件中执行命令：

`qalc --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件</span>
