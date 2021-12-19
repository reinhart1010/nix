---
layout: page
title: osx/wacaw (中文)
description: "一个用于 macOS 的小命令行工具，允许您从连接的摄像头捕获静止图片和视频。"
content_hash: bab1e6d515cd648be2791f4e989def1dffea9356
related_topics:
  - title: English version
    url: /en/osx/wacaw.html
    icon: bi bi-globe
---
# wacaw

一个用于 macOS 的小命令行工具，允许您从连接的摄像头捕获静止图片和视频。
更多信息：<http://webcam-tools.sourceforge.net>.

- 从网络摄像机拍照：

`wacaw `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 录制视频：

`wacaw --video `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>` -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">录制多少秒</span>

- 用自定义分辨率拍照：

`wacaw -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">宽</span>` -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">高</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件名</span>

- 将刚拍摄的图像复制到剪贴板：

`wacaw --to-clipboard`

- 可用设备列表：

`wacaw -L`
