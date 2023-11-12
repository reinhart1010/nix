---
layout: page
title: osx/system_profiler (中文)
description: "报告系统硬件和软件配置。"
content_hash: da7de93d316b1554e4b6a5c53dc39a2dd0583c43
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/system_profiler.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># system_profiler

报告系统硬件和软件配置。
更多信息：<https://ss64.com/osx/system_profiler.html>.

- 显示可由 System Profiler.app 打开的完整系统资源报告：

`system_profiler -xml > MyReport.spx`

- 显示硬件概述（型号、CPU、内存、串行等）：

`system_profiler SPHardwareDataType`

- 打印系统序列号：

`system_profiler SPHardwareDataType|grep "Serial Number (system)" |awk '{print $4}'`
