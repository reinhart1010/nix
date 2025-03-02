---
layout: page
title: common/youtube-viewer (中文)
description: "搜索并播放 YouTube 上的视频。"
content_hash: 0525d830578564fcd2dcfd8b861cec07bf4fce53
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/youtube-viewer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/youtube-viewer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# youtube-viewer

搜索并播放 YouTube 上的视频。
请参阅：`you-get`，`ytfzf`，`yt-dlp`。
更多信息：<https://github.com/trizen/youtube-viewer>.

- 搜索一个视频：

`youtube-viewer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">搜索关键词</span>

- 登录到你的 YouTube 账户：

`youtube-viewer --login`

- 在 VLC 中观看指定 URL 的视频：

`youtube-viewer --player=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vlc</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://youtube.com/watch?v=dQw4w9WgXcQ</span>

- 显示一个搜索提示并以 720p 播放已选视频：

`youtube-viewer -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7</span>
