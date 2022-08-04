---
layout: page
title: windows/cmstp (中文)
description: "用于管理连接服务配置文件的命令行工具。"
content_hash: 6bc9f529f30a0eccc1a2133d25d53ac7443d6877
related_topics:
  - title: English version
    url: /en/windows/cmstp.html
    icon: bi bi-globe
---
# cmstp

用于管理连接服务配置文件的命令行工具。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- 安装指定的配置文件：

`cmstp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 安装时不创建桌面快捷方式：

`cmstp /ns "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 安装时不检查依赖：

`cmstp /nf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 仅为当前用户安装：

`cmstp /su "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 为所有用户安装（需要管理员权限）：

`cmstp /au "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 静默安装：

`cmstp /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 卸载一个指定的配置文件：

`cmstp /u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`

- 静默删除：

`cmstp /u /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">配置文件的路径</span>`"`
