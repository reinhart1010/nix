---
layout: page
title: common/asciinema (中文)
description: "录制和重放终端会话，并可以选择将其分享在 <https://asciinema.org> 上。"
content_hash: 5f97a38533d7ca39ce7cf50108a961a0e915314d
last_modified_at: 2024-11-27
related_topics:
  - title: English version
    url: /en/common/asciinema.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/asciinema.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciinema.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/asciinema.html
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
tldri18n_status: 2
---
# asciinema

录制和重放终端会话，并可以选择将其分享在 <https://asciinema.org> 上。
请参阅：`terminalizer`。
更多信息：<https://docs.asciinema.org/manual/cli/usage>.

- 将本地安装的`asciinema`与 asciinema.org 账号关联：

`asciinema auth`

- 进行新的录制（使用 `Ctrl+D` 完成录制或键入 `exit`，然后选择上传或保存到本地）：

`asciinema rec`

- 进行新的录制，保存到本地的文件中：

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/录制文件.cast</span>

- 从本地文件中播放终端录屏：

`asciinema play `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/录制文件.cast</span>

- 在 <https://asciinema.org> 中播放终端录屏：

`asciinema play https://asciinema.org/a/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">文件 ID</span>

- 进行新的录制，将闲置时间设置为最多 2.5 秒：

`asciinema rec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-i|--idle-time-limit</span>` 2.5`

- 打印本地保存的录像的完整输出：

`asciinema cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/录制文件.cast</span>

- 从本地上传一个录屏到 asciinema.org：

`asciinema upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/录制文件.cast</span>
