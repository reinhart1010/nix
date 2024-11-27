---
layout: page
title: common/feh (中文)
description: "轻量级图像查看工具。"
content_hash: fde14ba3c5a99e6c36f8e62bef2e6a3f077173b9
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/feh.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/feh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/feh.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># feh

轻量级图像查看工具。
更多信息：<https://feh.finalrewind.org>.

- 查看本地图像或使用 URL：

`feh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 递归查看图像：

`feh --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 使用无边框窗口查看图像：

`feh --borderless `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 在浏览完最后一个图像之后退出：

`feh --cycle-once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 设置幻灯片放映周期延迟时间（秒）：

`feh --slideshow-delay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 设置墙纸（居中、填充、最大化、缩放或平铺）：

`feh --bg-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">center|fill|max|scale|tile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/图像</span>

- 创建目录中所有图像的拼贴，并作为新图像输出：

`feh --montage --thumb-height `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --thumb-width `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">150</span>` --index-info "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">%nn%wx%h</span>`" --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/拼贴图像.png</span>
