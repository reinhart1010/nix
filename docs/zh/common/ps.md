---
layout: page
title: common/ps (中文)
description: "提供正在运行的进程的信息。"
content_hash: d68c7d6538793f6f3787ded272d2aba88194f668
last_modified_at: 2024-01-08
related_topics:
  - title: English version
    url: /en/common/ps.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/ps.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/ps.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ps.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ps.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ps.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ps

提供正在运行的进程的信息。
更多信息: <https://manned.org/ps>.

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 查找与字符串匹配的进程：

`ps aux | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">字符串</span>

- 以 extra full 格式列出当前用户的所有进程：

`ps --user $(id -u) -F`

- 以树形方式列出当前用户的所有进程：

`ps --user $(id -u) f`

- 获取一个进程的父进程 ID：

`ps -o ppid= -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">进程 ID</span>

- 按内存使用量对进程进行排序：

`ps --sort size`
