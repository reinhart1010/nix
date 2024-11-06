---
layout: page
title: common/screen (中文)
description: "在远程服务器上保持会话打开。通过单个 SSH 连接管理多个窗口。"
content_hash: c291b36d9bece61b4a6e7008c946e8ff75d05c70
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/screen.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/screen.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># screen

在远程服务器上保持会话打开。通过单个 SSH 连接管理多个窗口。
类似工具请参阅 `tmux` 和 `zellij`。
更多信息：<https://manned.org/screen>.

- 启动一个新的 screen 会话：

`screen`

- 启动一个指定名称的新 screen 会话：

`screen -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名称</span>

- 启动一个后台会话，指定会话名称并执行指定命令并将日志输出到 screenlog.x：

`screen -dmLS `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 显示所有打开的 screen 会话：

`screen -ls`

- 重新连接到一个打开的 screen 会话：

`screen -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名称</span>

- 从当前 screen 会话中分离（先按 `Ctrl + A` 然后按 `D` 分离会话）：

`<Ctrl> + A, D`

- 关闭当前 screen 会话：

`<Ctrl> + A, K`

- 关闭一个已经分离的 screen 会话：

`screen -X -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名称</span>` quit`
