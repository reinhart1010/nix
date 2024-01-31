---
layout: page
title: osx/scutil (English)
description: "Manage system configuration parameters."
content_hash: 88a1134856e630c272f287dcd0bac10606468182
last_modified_at: 2024-01-31
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
Necessitates to be root when setting configuration.
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
