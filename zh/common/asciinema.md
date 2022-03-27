---
layout: page
title: common/asciinema (中文)
description: "录制和播放终端会话，也可以把他们分享到 asciinema.org."
content_hash: 9b0a13ce7cff1da41ebf919e692e291f72a67128
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/asciinema.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciinema.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/asciinema.html
    icon: bi bi-globe
---
# asciinema

录制和播放终端会话，也可以把他们分享到 asciinema.org.
更多信息：<https://asciinema.org/>.

- 将本地安装的`asciinema`与 asciinema.org 账号关联：

`asciinema auth`

- 进行新的录制（完成后，将提示用户上传或在本地保存）：

`asciinema rec`

- 进行新的录制，保存到本地的文件中：

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>`.cast`

- 从本地文件中播放终端录屏：

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>`.cast`

- 在 asciinema.org 中播放终端录屏：

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 ID</span>

- 进行新的录制，将闲置时间设置为最多 2.5 秒：

`asciinema rec -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.5</span>

- 打印本地保存的录像的完整输出：

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>`.cast`

- 从本地上传一个录屏到 asciinema.org：

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件路径</span>`.cast`
