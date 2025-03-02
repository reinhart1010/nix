---
layout: page
title: common/gendesk (中文)
description: "通过指定少量信息的命令来生成`.desktop`文件以及下载图标。"
content_hash: 4470a2921daa497afba7ed6b5dfb2d235158acf0
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gendesk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gendesk

通过指定少量信息的命令来生成`.desktop`文件以及下载图标。
更多信息：<https://gendesk.roboticoverlords.org>.

- 创建一个名为`应用程序`的`.desktop`文件：

`gendesk -n --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序</span>`" --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/应用程序</span>`" --icon "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/图标.png</span>`" --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">这是一个应用程序</span>`"`

- 创建一个名为`应用程序`的`.desktop`文件, 不显示任何输出，如果存在则覆盖同名文件：

`gendesk -q -f -n --name "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用程序</span>`" --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/应用程序</span>`" --icon "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/路径/到/图标.png</span>`" --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">这是一个应用程序</span>`"`

- 显示帮助信息：

`gendesk -h`
