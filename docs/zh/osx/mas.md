---
layout: page
title: osx/mas (中文)
description: "Mac 应用商店的命令行界面。"
content_hash: 4c22ea37dd036fa24554b41335175246fecf32f3
related_topics:
  - title: English version
    url: /en/osx/mas.html
    icon: bi bi-globe
---
# mas

Mac 应用商店的命令行界面。
更多信息：<https://github.com/mas-cli/mas>.

- 首次登录 Mac 应用商店：

`mas signin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user@example.com</span>

- 显示所有已安装的应用程序和它们的产品标识符：

`mas list`

- 搜索一个应用程序，在结果旁边显示价格：

`mas search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序</span>` --price`

- 安装或更新一个应用程序：

`mas install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">产品标识符</span>

- 安装所有待定的更新：

`mas upgrade`
