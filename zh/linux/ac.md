---
layout: page
title: linux/ac (中文)
description: "打印用户连接时长数据。"
content_hash: 53b1a9b6b94345793c8d412df2e9493204197cb9
related_topics:
  - title: Deutsch version
    url: /de/linux/ac.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/ac.html
    icon: bi bi-globe
---
# ac

打印用户连接时长数据。
更多信息：<https://www.gnu.org/software/acct/manual/accounting.html#ac>.

- 以小时为单位打印当前用户连接时间：

`ac`

- 以小时为单位打印所有用户连接时间：

`ac --individual-totals`

- 以小时为单位打印特定用户连接时间：

`ac --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 以小时为单位打印特定用户每天连接时间：

`ac --daily-totals --individual-totals `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>

- 显示附加明细：

`ac --compatibility`
