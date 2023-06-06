---
layout: page
title: common/git-config (中文)
description: "管理 Git 仓库的自定义设置项。"
content_hash: 935913eb61c3387e6c9cc2c9746201280b3df1da
last_modified_at: 2023-06-06
related_topics:
  - title: Deutsch version
    url: /de/common/git-config.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-config.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-config.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-config.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-config.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-config.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-config.html
    icon: bi bi-globe
---
# git config

管理 Git 仓库的自定义设置项。
这些设置可以分为局部设置（只对当前仓库生效）和全局设置（对当前用户生效）。
更多信息：<https://git-scm.com/docs/git-config>.

- 列出局部设置项（存储在当前仓库的 `.git/config`）：

`git config --list --local`

- 列出全局配置项（存储在 `~/.gitconfig`）：

`git config --list --global`

- 列出系统配置项（存储在 `/etc/gitconfig`），并且展示文件的位置：

`git config --list --system --show-origin`

- 获取某个配置项的值：

`git config alias.unstage`

- 设置某个全局配置项：

`git config --global alias.unstage "reset HEAD --"`

- 将某个全局配置项恢复为默认值：

`git config --global --unset alias.unstage`

- 使用默认编辑器修改本地设置：

`git config --edit`

- 使用默认编辑器修改全局设置：

`git config --global --edit`
