---
layout: page
title: windows/ipconfig (English)
description: "Display and manage the network configuration of Windows."
content_hash: ab3d788a6294854b93b2c863851e01e45835dbc4
related_topics:
  - title: Indonesia version
    url: /id/windows/ipconfig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/ipconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/ipconfig.html
    icon: bi bi-globe
---
# ipconfig

Display and manage the network configuration of Windows.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Show a list of network adapters:

`ipconfig`

- Show a detailed list of network adapters:

`ipconfig /all`

- Renew the IP addresses for a network adapter:

`ipconfig /renew `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Free up the IP addresses for a network adapter:

`ipconfig /release `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">adapter</span>

- Remove all data from the DNS cache:

`ipconfig /flushdns`
