---
layout: page
title: common/runsvdir (中文)
description: "运行整个目录下的服务。"
content_hash: 1df0034486c767fc95604948abc6ac3ef1b143d4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/runsvdir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runsvdir

运行整个目录下的服务。
更多信息：<https://manned.org/runsvdir.8>.

- 以当前用户身份启动和管理目录中的所有服务：

`runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 以 root 用户身份启动和管理目录中的所有服务：

`sudo runsvdir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>

- 在单独会话中启动服务：

`runsvdir -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/服务目录</span>
