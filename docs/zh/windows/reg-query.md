---
layout: page
title: windows/reg-query (中文)
description: "显示注册表中键和子键的值。"
content_hash: 48f1434a606b7f2056c038a0e7a437886def10c8
related_topics:
  - title: English version
    url: /en/windows/reg-query.html
    icon: bi bi-globe
---
# reg query

显示注册表中键和子键的值。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- 显示一个键中的所有值：

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>

- 显示键中指定的值：

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">值</span>

- 显示指定键和其子键中的所有的值：

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /s`

- 搜索与特定模式匹配的键和值：

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">查询语句</span>`"`

- 显示与指定数据类型匹配的键的值：

`reg query `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">键名</span>` /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">类型</span>
