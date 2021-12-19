---
layout: page
title: windows/getmac (中文)
description: "显示系统的 MAC 地址。"
content_hash: ca561e41f86ecb1c52e27081bed6e643417a992f
related_topics:
  - title: English version
    url: /en/windows/getmac.html
    icon: bi bi-globe
---
# getmac

显示系统的 MAC 地址。
更多信息：<https://docs.microsoft.com/windows-server/administration/windows-commands/getmac>.

- 显示当前系统的 MAC 地址：

`getmac`

- 以特定格式显示详细信息：

`getmac /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- 排除输出列表中的标题：

`getmac /nh`

- 显示一个远程主机的 MAC 地址：

`getmac /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">主机名</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">用户名</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">密码</span>

- 详细显示 MAC 地址信息：

`getmac /v`

- 显示详细的帮助信息：

`getmac /?`
