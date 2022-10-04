---
layout: page
title: windows/reg-compare (中文)
description: "比较注册表中的键和值。"
content_hash: c72253701b8638a8c20ec289956ab2b6b0cb90b7
related_topics:
  - title: English version
    url: /en/windows/reg-compare.html
    icon: bi bi-globe
---
# reg compare

比较注册表中的键和值。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- 比较两个键中的所有值：

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一个键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第二个键名</span>

- 比较两个键中指定的值：

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一个键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第二个键名</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 比较两个键中的所有子键和值：

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一个键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第二个键名</span>` /s`

- 仅输出指定键之间匹配的结果：

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一个键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第二个键名</span>` /os`

- 输出两个键之间的匹配和差异：

`reg compare `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第一个键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">第二个键名</span>` /oa`
