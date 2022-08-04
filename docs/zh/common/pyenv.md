---
layout: page
title: common/pyenv (中文)
description: "在多个 Python 版本之间轻松切换。"
content_hash: e78aa6e1b513346c7f730ee528cdfe4af23d175e
related_topics:
  - title: English version
    url: /en/common/pyenv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/pyenv.html
    icon: bi bi-globe
---
# pyenv

在多个 Python 版本之间轻松切换。
更多信息：<https://github.com/pyenv/pyenv>.

- 列出所有可用的命令：

`pyenv commands`

- 列出 `${PYENV_ROOT}/versions` 目录下的所有 Python 版本：

`pyenv versions`

- 在 `${PYENV_ROOT}/versions` 目录下安装一个 Python 版本：

`pyenv install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 在 `${PYENV_ROOT}/versions` 目录下卸载一个 Python 版本：

`pyenv uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 设置在当前机器中全局使用的 Python 版本：

`pyenv global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>

- 设置在当前目录及其下所有目录中使用的 Python 版本：

`pyenv local `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.7.10</span>
