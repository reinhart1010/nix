---
layout: page
title: common/ssh (中文)
description: "安全 Shell 是一种用于安全登录远程系统的协议。"
content_hash: 5f91444dae9cb35b6fc3c7ad2445eb30bb1d6c75
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/ssh.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/ssh.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/ssh.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ssh.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh

安全 Shell 是一种用于安全登录远程系统的协议。
它可用于在远程服务器上记录或执行命令。
更多信息：<https://man.openbsd.org/ssh>.

- 连接到远程服务器：

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>

- 使用特定身份（私钥）连接到远程服务器：

`ssh -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">路径/到/私钥文件</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>

- 使用指定端口号连接到远程服务器：

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口号</span>

- 在具有伪终端分配的远程服务器上运行命令，允许与远程命令进行交互：

`ssh `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">命令参数</span>

- SSH 隧道：动态端口转发（`localhost:1080` 上的 SOCKS 代理）：

`ssh -D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>

- SSH 隧道：转发特定端口（`localhost:9999` 到 `example.org:80`）以及禁用伪终端分配和远程命令的执行：

`ssh -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">9999</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.org</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>` -N -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>

- SSH 转发：通过跳转主机连接到远程服务器（可以指定多个跳转，以逗号分隔）：

`ssh -J `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">跳转主机地址</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机地址</span>

- 关闭挂起的会话：

`<回车键> ~ .`
