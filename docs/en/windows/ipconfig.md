---
layout: page
title: windows/ipconfig (English)
description: "Display and manage the network configuration of Windows."
content_hash: 5a7803cfb75159fb9e3a329b25d175e7bbdd3019
last_modified_at: 2023-07-12
related_topics:
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/ipconfig.html
    icon: bi bi-globe
---
# ipconfig

Display and manage the network configuration of Windows.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Show a list of network adapters:

`ipconfig`

- Show a detailed list of network adapters:

`ipconfig /all`

- Renew the IP addresses for a network adapter:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Free up the IP addresses for a network adapter:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Show the local DNS cache:

`ipconfig /displaydns`

- Remove all data from the local DNS cache:

`ipconfig /flushdns`
