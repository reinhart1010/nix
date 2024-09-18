---
layout: page
title: linux/apache2ctl (中文)
description: "Apache HTTP web 服务器命令行管理工具。"
content_hash: 7d8ec1cc4f915b109da7572f6a9201127f8b4e71
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apache2ctl

Apache HTTP web 服务器命令行管理工具。
基于 Debian 的操作系统自带该命令，基于 RHEL 的查看 `httpd`。
更多信息：<https://manned.org/apache2ctl.8>.

- 启动 Apache 守护进程。如果已运行则发送一个消息：

`sudo apache2ctl start`

- 关闭 Apache 守护进程：

`sudo apache2ctl stop`

- 重启 Apache 守护进程：

`sudo apache2ctl restart`

- 检查配置文件语法：

`sudo apache2ctl -t`

- 列出已加载模块：

`sudo apache2ctl -M`
