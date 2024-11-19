---
layout: page
title: common/uv-python (中文)
description: "管理 Python 版本和安装。"
content_hash: 60915d132d24e73380cce4310b9d483b09518e0e
last_modified_at: 2024-11-19
related_topics:
  - title: English version
    url: /en/common/uv-python.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/uv-python.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uv-python.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uv-python.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uv python

管理 Python 版本和安装。
更多信息：<https://docs.astral.sh/uv/reference/cli/#uv-python>.

- 列出所有可用的 Python 安装：

`uv python list`

- 安装某个版本的 Python：

`uv python install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 卸载某个版本的 Python：

`uv python uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 搜索某个版本的 Python 安装：

`uv python find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 锁定当前项目使用特定版本的 Python：

`uv python pin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本</span>

- 显示 `uv` Python 安装目录：

`uv python dir`
