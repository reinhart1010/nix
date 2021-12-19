---
layout: page
title: windows/logoff (中文)
description: "注销登录会话。"
content_hash: 6868180bbad280a5765609b1e2946213f70a7c74
related_topics:
  - title: English version
    url: /en/windows/logoff.html
    icon: bi bi-globe
---
# logoff

注销登录会话。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/logoff>.

- 注销当前会话：

`logoff`

- 通过名称和 id 注销会话：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名|会话 id</span>

- 在通过 RDP 连接的特定服务器上注销会话：

`logoff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">会话名|会话 id</span>` /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名</span>
