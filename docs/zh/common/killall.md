---
layout: page
title: common/killall (中文)
description: "根据进程名称向所有实例发送终止信号（必须是精确的进程名称）。"
content_hash: 28dc6ec36d565143ecb79567f61a39716f4f2524
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/killall.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/killall.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/killall.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/killall.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># killall

根据进程名称向所有实例发送终止信号（必须是精确的进程名称）。
除了 SIGKILL 和 SIGSTOP，所有信号都可以被进程拦截，从而实现正常退出。
更多信息：<https://manned.org/killall>.

- 使用默认的 SIGTERM（终止）信号结束进程：

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名称</span>

- 列出可用的信号名称（使用时无需加 `SIG` 前缀）：

`killall -l`

- 交互式地询问确认后再终止进程：

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名称</span>

- 使用 SIGINT（中断）信号终止进程，与按下 `Ctrl + C` 发送的信号相同：

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名称</span>

- 强制杀死一个进程：

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程名称</span>
