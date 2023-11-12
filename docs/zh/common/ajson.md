---
layout: page
title: common/ajson (中文)
description: "对 JSON 对象执行 JSONPath 操作。"
content_hash: 5e870b371d723dd903eef2c29f20ca6992d287e2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/ajson.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ajson.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ajson.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ajson.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ajson

对 JSON 对象执行 JSONPath 操作。
更多信息：<https://github.com/spyzhov/ajson>.

- 从文件中读取 JSON 并执行指定的 JSONPath 表达式：

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.json</span>

- 从标准输入中读取 JSON 并执行指定的 JSONPath 表达式：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/文件.json</span>` | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$..json[?(@.path)]</span>`'`

- 从 URL 中获取 JSON 并计算指定的 JSONPath 表达式：

`ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">avg($..price)</span>`' '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/api/</span>`'`

- 读取一些简单的 JSON 并计算一个值：

`echo '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>`' | ajson '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2 * pi * $</span>`'`
