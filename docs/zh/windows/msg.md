---
layout: page
title: windows/msg (中文)
description: "向指定的用户或会话发送信息。"
content_hash: 67e2cdb0d4bbae5377cbd92bc646179911269496
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/windows/msg.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/msg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# msg

向指定的用户或会话发送信息。
更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/msg>.

- 向指定的用户或会话发送信息：

`msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名|会话名|会话 id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">信息</span>

- 从标准输入发送信息：

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">信息</span>`" | msg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名|会话名|会话 id</span>

- 向指定的服务器发送消息：

`msg /server:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">服务器名称</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名|会话名|会话 id</span>

- 向当前计算机的所有用户发送消息：

`msg *`

- 设置发送消息的延迟：

`msg /time:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">秒</span>
