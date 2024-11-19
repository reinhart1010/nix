---
layout: page
title: common/uv-tool (中文)
description: "安装和运行由 Python 软件包提供的命令。"
content_hash: f3dc5fa671268a33e5c206d2db872908ef3731d3
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/uv-tool.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uv-tool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uv-tool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uv tool

安装和运行由 Python 软件包提供的命令。
更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-tool>.

- 运行一个来自软件包的命令，而不安装它：

`uv tool run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 在系统范围内安装一个 Python 软件包：

`uv tool install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 升级已安装的 Python 软件包：

`uv tool upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 卸载一个 Python 软件包：

`uv tool uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 列出系统范围内已安装的 Python 软件包：

`uv tool list`
