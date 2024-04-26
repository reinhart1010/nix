---
layout: page
title: osx/scutil (English)
description: "Manage system configuration parameters."
content_hash: 71cd572f01d1fce355b0294c3559ceaf96446dac
last_modified_at: 2024-04-26
related_topics:
  - title: español version
    url: /es/osx/scutil.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/scutil.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/scutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# scutil

Manage system configuration parameters.
Require root privileges when setting configuration.
More information: <https://keith.github.io/xcode-man-pages/scutil.8.html>.

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
