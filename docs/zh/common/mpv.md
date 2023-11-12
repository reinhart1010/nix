---
layout: page
title: common/mpv (中文)
description: "一个基于 MPlayer 的音频/视频播放器。"
content_hash: 62c7effd3fac439365456b32d7a8eff2af9d02e3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/mpv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mpv

一个基于 MPlayer 的音频/视频播放器。
更多信息：<https://mpv.io>.

- 播放一个音频或视频文件：

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 往后/往前 跳跃 5 秒：

`LEFT <or> RIGHT`

- 往后/往前 跳跃一分钟：

`DOWN <or> UP`

- 减少/增加 10% 播放速度：

`[ <or> ]`

- 以指定速度播放文件（0.01 到 100, 默认是 1）：

`mpv --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">速度</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 用 `mpv.conf` 中指定的一个用户配制播放文件：

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配制名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 播放摄像头或其他设备的输出：

`mpv /dev/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">video0</span>
