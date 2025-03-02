---
layout: page
title: common/josm (中文)
description: "可扩展的 OpenStreetMap 编辑器，适用于 Java 8+。"
content_hash: 1c26f33e05089d7726105969d2c74091c7d8827b
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/josm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/josm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/josm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# josm

可扩展的 OpenStreetMap 编辑器，适用于 Java 8+。
更多信息：<https://josm.openstreetmap.de/>.

- 启动 JOSM：

`josm`

- 在最大化模式下启动 JOSM：

`josm --maximize`

- 启动 JOSM 并设置特定的语言：

`josm --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de</span>

- 启动 JOSM 并将所有首选项重置为默认值：

`josm --reset-preferences`

- 启动 JOSM 并下载指定的边界框：

`josm --download `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- 启动 JOSM 并以原始 GPS 格式下载指定的边界框：

`josm --downloadgps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">minlat,minlon,maxlat,maxlon</span>

- 启动 JOSM 并且不加载插件：

`josm --skip-plugins`
