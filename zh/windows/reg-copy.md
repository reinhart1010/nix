---
layout: page
title: windows/reg-copy (中文)
description: "复制注册表中的键和值。"
content_hash: b71edc1b966c41325b377b5b262057a31696ed4a
related_topics:
  - title: English version
    url: /en/windows/reg-copy.html
    icon: bi bi-globe
---
# reg copy

复制注册表中的键和值。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- 将注册表键复制到新的注册表位置：

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">旧键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新键名</span>

- 递归将注册表键复制到新的注册表位置：

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">旧键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新键名</span>` /s`

- 在没有提示的情况下强制复制注册表键：

`reg copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">旧键名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新键名</span>` /f`
