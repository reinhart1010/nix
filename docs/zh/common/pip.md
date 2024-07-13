---
layout: page
title: common/pip (中文)
description: "Python 主流的包安装管理工具。"
content_hash: a97dffd21ab57bd5e2b6a87907c0ac81604918b7
last_modified_at: 2024-07-13
related_topics:
  - title: Deutsch version
    url: /de/common/pip.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/pip.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pip.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip

Python 主流的包安装管理工具。
更多信息：<https://pip.pypa.io/>.

- 安装包（通过 `pip install` 查看更多安装示例）：

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 安装包到用户目录而不是系统范围的默认位置：

`pip install --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 升级包：

`pip install --upgrade `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 卸载包：

`pip uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 将已安装的包以 Requirements 的格式保存文件中：

`pip freeze > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- 查看包的详细信息：

`pip show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 通过依赖文件（如 requirements.txt）来进行安装：

`pip install --requirement `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>
