---
layout: page
title: linux/shutdown (English)
description: "Shutdown and reboot the system."
content_hash: 3a91f38f350ac6c5c1f5d18e2fe7fbcdae382cdb
last_modified_at: 2023-12-03
related_topics:
  - title: català version
    url: /ca/linux/shutdown.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

Shutdown and reboot the system.
More information: <https://manned.org/shutdown.8>.

- Power off ([h]alt) immediately:

`shutdown -h now`

- [r]eboot immediately:

`shutdown -r now`

- [r]eboot in 5 minutes:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Shutdown at 1:00 pm (Uses 24[h] clock):

`shutdown -h 13:00`

- [c]ancel a pending shutdown/reboot operation:

`shutdown -c`
