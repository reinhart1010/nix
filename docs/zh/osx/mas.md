---
layout: page
title: osx/mas (中文)
description: "Mac 应用商店的命令行界面。"
content_hash: a3730ec7c13d13f538ce176c8199c4cd4e0a7b41
last_modified_at: 2024-08-20
related_topics:
  - title: English version
    url: /en/osx/mas.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mas.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mas

Mac 应用商店的命令行界面。
更多信息：<https://github.com/mas-cli/mas>.

- 首次登录 Mac 应用商店：

`mas signin "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>`"`

- 显示所有已安装的应用程序和它们的产品标识符：

`mas list`

- 搜索一个应用程序，在结果旁边显示价格：

`mas search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序</span>`" --price`

- 安装或更新一个应用程序：

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">产品标识符</span>

- 安装所有待定的更新：

`mas upgrade`
