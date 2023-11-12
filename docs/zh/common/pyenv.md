---
layout: page
title: common/pyenv (中文)
description: "在多个 Python 版本之间轻松切换。"
content_hash: 38be409c2445156f0073e7fa6f210df6bc73db3e
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/pyenv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pyenv

在多个 Python 版本之间轻松切换。
更多信息：<https://github.com/pyenv/pyenv>.

- 列出所有可用的命令：

`pyenv commands`

- 列出 `${PYENV_ROOT}/versions` 目录下的所有 Python 版本：

`pyenv versions`

- 列出所有可以从上游安装的 Python 版本：

`pyenv install --list`

- 在 `${PYENV_ROOT}/versions` 目录下安装一个 Python 版本：

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 在 `${PYENV_ROOT}/versions` 目录下卸载一个 Python 版本：

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 设置在当前机器中全局使用的 Python 版本：

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 设置在当前目录及其下所有目录中使用的 Python 版本：

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
