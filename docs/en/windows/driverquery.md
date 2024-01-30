---
layout: page
title: windows/driverquery (English)
description: "Display information about installed device drivers."
content_hash: 044fe8f462cc1aad7184778c4c5bc6189d32b5d4
last_modified_at: 2024-01-30
related_topics:
  - title: 中文 version
    url: /zh/windows/driverquery.html
    icon: bi bi-globe
tldri18n_status: 2
---
# driverquery

Display information about installed device drivers.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/driverquery>.

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

- Display help:

`driverquery /?`
