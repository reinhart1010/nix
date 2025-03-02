---
layout: page
title: common/you-get (中文)
description: "从网络下载媒体内容（视频、音频、图像）。"
content_hash: b4c050f0774654a81ae825643e0a5a3a7480f555
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/you-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/you-get.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/you-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# you-get

从网络下载媒体内容（视频、音频、图像）。
请参阅：`yt-dlp`，`youtube-viewer`，`instaloader`。
更多信息：<https://you-get.org>.

- 打印网络上指定媒体的媒体信息：

`you-get --info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- 从指定 URL 下载媒体：

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/video?id=value</span>

- 在 Google 视频上搜索并下载：

`you-get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">关键词</span>

- 将媒体下载到指定位置：

`you-get --output-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` --output-filename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>

- 使用代理下载媒体：

`you-get --http-proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">代理服务器</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/watch?v=value</span>
