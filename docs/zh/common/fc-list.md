---
layout: page
title: common/fc-list (中文)
description: "列出系统上安装的可用字体。"
content_hash: 92452bf72c1613d0872b4c2f2f76a334a24cb63d
related_topics:
  - title: English version
    url: /en/common/fc-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc-list.html
    icon: bi bi-globe
---
# fc-list

列出系统上安装的可用字体。
更多信息：<https://manned.org/fc-list>.

- 返回系统中已安装字体的列表：

`fc-list`

- 返回具有给定名称的已安装字体的列表：

`fc-list | grep '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">DejaVu Serif</span>`'`

- 返回系统中已安装字体的数量：

`fc-list | wc -l`
