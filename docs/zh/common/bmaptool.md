---
layout: page
title: common/bmaptool (中文)
description: "便捷地创建或复制块文件映射（被设计的比`cp`或`dd`更快）。"
content_hash: 60092b64229cf2bc4d3ce4c8395446fa5f1fba61
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bmaptool.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bmaptool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bmaptool.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bmaptool

便捷地创建或复制块文件映射（被设计的比`cp`或`dd`更快）。
更多信息：<https://source.tizen.org/documentation/reference/bmaptool>.

- 使用图片生成块图文件：

`bmaptool create -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap 格式文件.bmap</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件</span>

- 复制图片到指定目录：

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap 格式文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/开发路径/sdb</span>

- 复制压缩后的图片到指定目录：

`bmaptool copy --bmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">blockmap 格式文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件.gz</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/开发路径/sdb</span>

- 复制图片的时候，不将图片转成块图：

`bmaptool copy --nobmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">图片文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/开发路径/sdb</span>
