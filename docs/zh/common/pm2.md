---
layout: page
title: common/pm2 (中文)
description: "Node.js 的进程管理工具。"
content_hash: d66644e040b74ad8d348519a7054cd5d12d3b45d
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/pm2.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/pm2.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pm2

Node.js 的进程管理工具。
用于日志管理、监控和配置进程。
更多信息：<https://pm2.keymetrics.io>.

- 启动一个进程并指定名称，以便后续操作使用：

`pm2 start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名称</span>

- 列出所有进程：

`pm2 list`

- 监控所有进程：

`pm2 monit`

- 停止一个进程：

`pm2 stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名称</span>

- 重启一个进程：

`pm2 restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">应用名称</span>

- 保存当前所有进程，便于稍后恢复：

`pm2 save`

- 恢复之前保存的进程：

`pm2 resurrect`
