---
layout: page
title: common/browser-sync (中文)
description: "启动一个本地的服务，可以监听文件改动，刷新浏览器。"
content_hash: 142ffceb495b4791bfa7de93631ddbfc6fbbee0c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/browser-sync.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/browser-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/browser-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# browser-sync

启动一个本地的服务，可以监听文件改动，刷新浏览器。
更多信息：<https://browsersync.io/docs/command-line>.

- 将指定目录发成服务：

`browser-sync start --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>` --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 启动当前目录服务，同时监听指定目录下 `css` 文件的变动：

`browser-sync start --server --files '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录/*.css</span>`'`

- 创建配置文件：

`browser-sync init`

- 按指定配置文件中的配置启动服务：

`browser-sync start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件</span>
