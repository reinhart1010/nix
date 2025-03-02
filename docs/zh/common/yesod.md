---
layout: page
title: common/yesod (中文)
description: "Yesod 是一个基于 Haskell 的网页框架的辅助工具。"
content_hash: baaa6a48a2a5de6ff01e3dc9005251f465c70810
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/yesod.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/yesod.html
    icon: bi bi-globe
tldri18n_status: 2
---
# yesod

Yesod 是一个基于 Haskell 的网页框架的辅助工具。
所有 Yesod 命令都通过 `stack` 项目管理器来调用。
更多信息：<https://github.com/yesodweb/yesod>.

- 在 `my-project` 目录下创建一个以 SQLite 为后端的新样板网站：

`stack new `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-project</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yesod-sqlite</span>

- 在一个 Yesod 样板网站中安装 Yesod CLI 工具：

`stack build yesod-bin cabal-install --install-ghc`

- 启动开发服务器：

`stack exec -- yesod devel`

- 处理具有更改的 Template Haskell 依赖项的文件：

`stack exec -- yesod touch`

- 使用 Keter（Yesod 的部署管理器）部署应用程序：

`stack exec -- yesod keter`
