---
layout: page
title: common/yadm (中文)
description: "一个通过使用 `git` 来管理 dotfiles 的工具。"
content_hash: 49b3852afe653802ffdc3e32181ae74b635c2e68
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yadm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yadm

一个通过使用 `git` 来管理 dotfiles 的工具。
此命令也有关于其子命令的文件，例如：`init`、`clone`、`push` 和 `pull`。
更多信息：<https://yadm.io/docs/overview>.

- 覆盖 `yadm` 目录。`yadm` 会相对于此目录存储其配置：

`yadm --yadm-dir`

- 覆盖 `yadm` 数据目录：`yadm` 会相对于此目录存储其数据：

`yadm --yadm-data`

- 覆盖 `yadm` 仓库的位置：

`yadm --yadm-repo`

- 覆盖 `yadm` 配置文件的位置：

`yadm --yadm-config`

- 覆盖 `yadm` 加密配置的位置：

`yadm --yadm-encrypt`

- 覆盖 `yadm` 加密文件归档的位置：

`yadm --yadm-archive`

- 覆盖 `yadm` 引导程序的位置：

`yadm --yadm-bootstrap`
