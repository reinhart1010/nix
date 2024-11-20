---
layout: page
title: common/qmmp (中文)
description: "具有类似于 Winamp 或 XMMS 界面的音频播放器。"
content_hash: af297012f7a3cf0a0b3071065d8ec804a1fd6ba2
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/qmmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/qmmp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# qmmp

具有类似于 Winamp 或 XMMS 界面的音频播放器。
请参阅：`clementine`，`ncmpcpp`，`cmus`。
更多信息：<https://qmmp.ylsoftware.com>.

- 启动 GUI：

`qmmp`

- 开始或停止当前播放的音频：

`qmmp --play-pause`

- 向前或向后移动指定的秒数：

`qmmp --seek-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fwd|bwd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒数</span>

- 播放下一个音频文件：

`qmmp --next`

- 播放上一个音频文件：

`qmmp --previous`

- 显示当前音量：

`qmmp --volume-status`

- 增加或减少当前播放音频的音量 5%：

`qmmp --volume-`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inc|dec</span>
