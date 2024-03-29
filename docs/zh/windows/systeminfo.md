---
layout: page
title: windows/systeminfo (中文)
description: "显示本地或远程计算机的操作系统配置。"
content_hash: 13d36dbf0f733aeb856937e7f4eb18487e1215b3
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/systeminfo.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/systeminfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systeminfo

显示本地或远程计算机的操作系统配置。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/systeminfo>.

- 显示本地计算机的操作系统配置：

`systeminfo`

- 以指定的输出格式显示系统配置：

`systeminfo /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 显示远程计算机的系统配置：

`systeminfo /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">远程主机名</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 显示详细的帮助信息：

`systeminfo /?`
