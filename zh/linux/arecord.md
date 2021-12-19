---
layout: page
title: linux/arecord (中文)
description: "ALSA 声卡驱动的声音录制器。"
content_hash: 1a4421fc72bb0a74dc5988b0c49f5dac5711e54a
related_topics:
  - title: Deutsch version
    url: /de/linux/arecord.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/arecord.html
    icon: bi bi-globe
---
# arecored

ALSA 声卡驱动的声音录制器。
更多信息：<https://manned.org/arecord>.

- 以 "CD" 质量录制一段声音（录制结束以 Ctrl-C 停止）：

`arecord -vv --format=cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件名.wav</span>

- 以 "CD" 质量录制 10 秒钟声音：

`arecord -vv --format=cd --duration=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件名.wav</span>

- 录制一段声音并以 mp3 格式保存（录制结束以 Ctrl-C 停止）：

`arecord -vv --format=cd --file-type raw | lame -r - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/文件名.mp3</span>

- 列出所有的声卡和数字音频设备：

`arecord --list-devices`

- 允许交互式界面（例如使用空格键或回车键来播放或暂停）：

`arecord --interactive`
