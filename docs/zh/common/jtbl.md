---
layout: page
title: common/jtbl (中文)
description: "用于在终端中将 JSON 和 JSON Lines 数据打印为表格的工具。"
content_hash: f9a1e8d6992c6abf2de6473eaad7cd420d33e16d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/jtbl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/jtbl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jtbl

用于在终端中将 JSON 和 JSON Lines 数据打印为表格的工具。
更多信息：<https://github.com/kellyjonbrazil/jtbl>.

- 从 JSON 或 JSON Lines 输入中打印表格：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jtbl`

- 打印表格并指定用于换行的列宽：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jtbl --cols=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宽度</span>

- 打印表格并截断行而不是换行：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jtbl -t`

- 打印表格并不换行或截断行：

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件.json</span>` | jtbl -n`
