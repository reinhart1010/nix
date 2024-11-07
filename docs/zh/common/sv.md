---
layout: page
title: common/sv (中文)
description: "控制一个正在运行的 runsv 服务。"
content_hash: 96eb623e685a3db8027a140f3b9d9faf1a7af7d3
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/sv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sv

控制一个正在运行的 runsv 服务。
更多信息：<https://manned.org/sv.8>.

- 启动服务：

`sudo sv up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 停止服务：

`sudo sv down `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 获取服务状态：

`sudo sv status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 重载服务：

`sudo sv reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 启动服务，但仅当它未运行时启动，停止后不自动重启：

`sudo sv once `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>
