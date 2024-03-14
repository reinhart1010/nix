---
layout: page
title: windows/logoff (中文)
description: "注销登录会话。"
content_hash: d1fc56d3acf439d84b69fb67833ad507eb449738
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/logoff.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/logoff.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/logoff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logoff

注销登录会话。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/logoff>.

- 注销当前会话：

`logoff`

- 通过名称和 ID 注销会话：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名|会话 id</span>

- 在通过 RDP 连接的特定服务器上注销会话：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名|会话 id</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>
