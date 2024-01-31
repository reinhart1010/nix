---
layout: page
title: osx/system_profiler (中文)
description: "报告系统硬件和软件配置。"
content_hash: dfd72c126b75e902b7ff5a1a5a5a85c476158e9c
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/system_profiler.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># system_profiler

报告系统硬件和软件配置。
更多信息：<https://keith.github.io/xcode-man-pages/system_profiler.8.html>.

- 显示可由 System Profiler.app 打开的完整系统资源报告：

`system_profiler -xml > MyReport.spx`

- 显示硬件概述（型号、CPU、内存、串行等）：

`system_profiler SPHardwareDataType`

- 打印系统序列号：

`system_profiler SPHardwareDataType|grep "Serial Number (system)" |awk '{print $4}'`
