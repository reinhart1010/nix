---
layout: page
title: common/zapier (中文)
description: "创建、自动化并管理 Zapier 集成。"
content_hash: c2ed8b87b88c582d3a975c6b6f968892e3ca5fb8
last_modified_at: 2024-12-05
related_topics:
  - title: English version
    url: /en/common/zapier.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/zapier.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zapier

创建、自动化并管理 Zapier 集成。
此命令也有关于其子命令的文件，例如：`build`，`init`，`scaffold`，`push`，`test`，等。
更多信息：<https://platform.zapier.com/reference/cli>.

- 连接到一个 Zapier 帐户：

`zapier login`

- 使用项目模板初始化一个新的 Zapier 集成：

`zapier init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/目录</span>

- 向你的集成中添加一个初始的触发器、创建、搜索或资源：

`zapier scaffold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">trigger|create|search|resource</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">名称</span>

- 测试一个集成：

`zapier test`

- 构建并上传一个集成到 Zapier：

`zapier push`

- 显示帮助：

`zapier help`

- 显示特定命令的帮助：

`zapier help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>
