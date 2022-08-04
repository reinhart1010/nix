---
layout: page
title: windows/systeminfo (中文)
description: "显示本地或远程计算机的操作系统配置。"
content_hash: 16d65bdd2bfac8017fe7d4321dd45938d3ddf33f
related_topics:
  - title: English version
    url: /en/windows/systeminfo.html
    icon: bi bi-globe
---
# systeminfo

显示本地或远程计算机的操作系统配置。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 显示本地计算机的操作系统配置：

`systeminfo`

- 以指定的输出格式显示系统配置：

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 显示远程计算机的系统配置：

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机名</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 显示详细的帮助信息：

`systeminfo /?`
