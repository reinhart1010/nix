---
layout: page
title: common/logger (中文)
description: "向系统日志增加记录（/var/log/syslog）。"
content_hash: 4bdb1f79653f2eee669d362ba2a2c5291b45ffc9
last_modified_at: 2024-01-01
related_topics:
  - title: English version
    url: /en/common/logger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logger

向系统日志增加记录（/var/log/syslog）。
更多信息：<https://manned.org/logger>.

- 向系统日志增加记录：

`logger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">消息内容</span>

- 从 `stdin` 获取输入并记录到系统日志 syslog：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">记录内容</span>` | logger`

- 将输出发送到在给定端口上运行的远程系统日志服务器。默认端口为 514：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">记录内容</span>` | logger --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口</span>

- 对记录的每一行使用特定的标签。默认值是登录用户的名：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">记录内容</span>` | logger --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">标签</span>

- 以给定的错误等级记录消息。默认是 `user.notice`. 使用 `man logger` 查询所有可选等级：

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">记录内容</span>` | logger --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.warning</span>
