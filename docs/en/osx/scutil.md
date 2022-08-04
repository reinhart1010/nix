---
layout: page
title: osx/scutil (English)
description: "Manage system configuration parameters."
content_hash: 82b2801f34bafa17fbe27f5b7b27b8f349e8bdb3
related_topics:
  - title: português (Portugal) version
    url: /pt_PT/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
---
# scutil

Manage system configuration parameters.
Necessitates to be root when setting configuration.
More information: <https://ss64.com/osx/scutil.html>.

- Display DNS Configuration:

`scutil --dns`

- Display proxy configuration:

`scutil --proxy`

- Get computer name:

`scutil --get ComputerName`

- Set computer name:

`sudo scutil --set ComputerName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_name</span>

- Get hostname:

`scutil --get HostName`

- Set hostname:

`scutil --set HostName `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>
