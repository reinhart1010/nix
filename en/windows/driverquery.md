---
layout: page
title: windows/driverquery (English)
description: "Display information about installed device drivers."
content_hash: 7a30f226793c5ab3e281a0e0e9e4899a2a4dc18a
related_topics:
  - title: 中文 version
    url: /zh/windows/driverquery.html
    icon: bi bi-globe
---
# driverquery

Display information about installed device drivers.
More information: <https://docs.microsoft.com/windows-server/administration/windows-commands/driverquery>.

- Display a list of all installed device drivers:

`driverquery`

- Display a list of drivers in the specified format:

`driverquery /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Display a list of drivers with a column to indicate if they are signed:

`driverquery /si`

- Exclude the header in the output list:

`driverquery /nh`

- Display a list of drivers for a remote machine:

`driverquery /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Display a list of drivers with verbose information:

`driverquery /v`

- Display detailed usage information:

`driverquery /?`
