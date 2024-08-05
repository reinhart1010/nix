---
layout: page
title: common/pip-install (中文)
description: "用于安装 Python 包。"
content_hash: ab9c84b114e8c62e9382e03247a29e6361f2461b
last_modified_at: 2024-08-05
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
tldri18n_status: 2
---
# pip install

用于安装 Python 包。
更多信息：<https://pip.pypa.io>.

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
