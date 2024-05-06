---
layout: page
title: common/nmap (中文)
description: "网络探索工具和安全/端口扫描程序。"
content_hash: 3e2a10adc458b02949b2873370fc05b0b0043fd8
last_modified_at: 2024-05-06
related_topics:
  - title: Deutsch version
    url: /de/common/nmap.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nmap.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/nmap.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nmap.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/nmap.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># nmap

网络探索工具和安全/端口扫描程序。
仅当以特权运行 Nmap 时，某些功能才激活。
更多信息：<https://nmap.org/book/man.html>.

- 检查 IP 地址是否可用，并猜测远程主机的操作系统：

`nmap -O `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP 或者 主机名</span>

- 尝试确定指定的主机是否启动以及它们的名称是什么：

`sudo nmap -sn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP 或者 主机名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可选的其它地址</span>

- 像上面一样，如果主机启动了，还可以运行默认的 1000 端口 TCP 扫描：

`nmap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP 或者 主机名</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">可选的其它地址</span>

- 也可以启用脚本，服务检测，操作系统指纹识别和跟踪路由：

`nmap -A `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">一个地址 或者 多个地址</span>

- 扫描端口的特定列表（使用 `-p` 参数覆盖所有端口，如 `-p 1-65535`，也可以明确指定几个端口，如 `-p 3306,3307,3308`）：

`nmap -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">端口1, 端口2, ..., 端口N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">一个地址 或者 多个地址</span>

- 使用默认 NSE 脚本执行针对该主机地址的完整端口、服务、版本检测扫描，以确定弱点和信息：

`nmap -sC -sV `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">一个地址 或者 多个地址</span>
