---
layout: page
title: windows/reg-delete (中文)
description: "从注册表中删除键和值。"
content_hash: 930a9ee1c9bb30a00f10dbeab47d65b68a1a06bc
related_topics:
  - title: English version
    url: /en/windows/reg-delete.html
    icon: bi bi-globe
---
# reg delete

从注册表中删除键和值。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- 删除一个指定的键：

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>

- 删除键中指定的值：

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 递归删除指定键下所有的值：

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /va`

- 在没有提示的情况下递归删除键中所有的值：

`reg delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /f /va`
