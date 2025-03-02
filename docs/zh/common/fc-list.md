---
layout: page
title: common/fc-list (中文)
description: "列出系统上安装的可用字体。"
content_hash: 808cf56d1c3ce1dc62cd6aaf1c0e3d6d67b41191
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/fc-list.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/fc-list.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fc-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fc-list.html
    icon: bi bi-globe
tldri18n_status: 2
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

- 返回支持指定语言（基于区域设置代码）的已安装字体列表：

`fc-list :lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jp</span>

- 返回包含指定 Unicode 码位字形的已安装字体列表：

`fc-list :charset=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">f303</span>
