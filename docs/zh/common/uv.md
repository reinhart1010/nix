---
layout: page
title: common/uv (中文)
description: "一个快速的 Python 软件包和项目管理器。"
content_hash: 1eb7d5385cf0c57c2037a622c88b01466d6fadb3
last_modified_at: 2024-11-20
related_topics:
  - title: English version
    url: /en/common/uv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/uv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uv

一个快速的 Python 软件包和项目管理器。
此命令也有关于其子命令的文件，例如：`tool` 和 `python`.
更多信息：<https://docs.astral.sh/uv/reference/cli>.

- 在当前目录中创建一个新的 Python 项目：

`uv init`

- 在具有指定名称的目录中创建一个新的 Python 项目：

`uv init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">项目名称</span>

- 向项目中添加一个新的软件包：

`uv add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 从项目中移除一个软件包：

`uv remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">软件包</span>

- 在项目的环境中运行一个脚本：

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/脚本.py</span>

- 在项目的环境中运行一个命令：

`uv run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>

- 从 `pyproject.toml` 更新项目的环境：

`uv sync`

- 为项目的依赖项创建一个锁定文件：

`uv lock`
