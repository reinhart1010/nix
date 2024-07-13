---
layout: page
title: common/pip-install (中文)
description: "用于安装 Python 包。"
content_hash: 16bb7aa9ed141da5665e9fec52b8384790720e35
last_modified_at: 2024-07-13
related_topics:
  - title: Deutsch version
    url: /de/common/pip-install.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pip-install.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/pip-install.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pip-install.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pip install

用于安装 Python 包。
更多信息：<https://pip.pypa.io/>.

- 安装包：

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>

- 安装指定版本的包：

`pip install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">包名</span>`==`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">版本号</span>

- 通过指定的依赖文件安装（通常文件名是 requirements.txt）：

`pip install -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">requirements.txt</span>

- 通过 URL 或源码存档文件安装（如 *.tar.gz 或 *.whl）：

`pip install --find-links `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|存档文件</span>

- 在本地的项目路径下以开发模式（editable）安装（通常是读取 pyproject.toml 或 setup.py 文件）：

`pip install --editable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>
