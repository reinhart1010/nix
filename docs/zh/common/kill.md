---
layout: page
title: common/kill (中文)
description: "向进程发送信号，通常用于停止进程。"
content_hash: b0eed9fa139680d946dd8c3c55eb5f661fbf7aab
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/kill.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/kill.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/kill.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/kill.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/kill.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/kill.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kill.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kill

向进程发送信号，通常用于停止进程。
除了 SIGKILL 和 SIGSTOP，所有信号都可以被进程拦截，以便进行正常退出。
更多信息：<https://manned.org/kill.1posix>.

- 使用默认的 SIGTERM（终止）信号来结束一个程序：

`kill `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程ID</span>

- 列出可用的信号名称（使用时无需加 `SIG` 前缀）：

`kill -l`

- 使用 SIGHUP（挂起）信号终止一个程序。许多守护进程接收到此信号后会重新加载而不是终止：

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1|HUP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程ID</span>

- 使用 SIGINT（中断）信号终止一个程序。通常由用户按下 `Ctrl + C` 发起：

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2|INT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程ID</span>

- 向操作系统发送信号，立即终止一个程序（程序无机会捕获信号）：

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9|KILL</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程ID</span>

- 向操作系统发送信号，暂停一个程序，直到收到 SIGCONT（继续）信号：

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">17|STOP</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程ID</span>

- 向所有具有指定 GID（组ID）的进程发送 `SIGUSR1` 信号：

`kill -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">SIGUSR1</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">组ID</span>
