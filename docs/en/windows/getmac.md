---
layout: page
title: windows/getmac (English)
description: "Display the MAC addresses of a system."
content_hash: 36d82a52e8fad9958010ac4c6a3be3769e053bf5
last_modified_at: 2023-11-12
related_topics:
  - title: español version
    url: /es/windows/getmac.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/getmac.html
    icon: bi bi-globe
tldri18n_status: 2
---
# getmac

Display the MAC addresses of a system.
More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/getmac>.

- Display the MAC addresses for the current system:

`getmac`

- Display the details in a specific format:

`getmac /fo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">table|list|csv</span>

- Exclude the header in the output list:

`getmac /nh`

- Display the MAC addresses for a remote machine:

`getmac /s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>

- Display the MAC addresses with verbose information:

`getmac /v`

- Display detailed usage information:

`getmac /?`
