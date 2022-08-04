---
layout: page
title: linux/shutdown (English)
description: "Shutdown and reboot the system."
content_hash: 4f7af9b4725788165b3ce1ca7aa77ec52a5f6eb5
related_topics:
  - title: español version
    url: /es/linux/shutdown.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/shutdown.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/shutdown.html
    icon: bi bi-globe
---
# shutdown

Shutdown and reboot the system.
More information: <https://manned.org/shutdown.8>.

- Power off (halt) immediately:

`shutdown -h now`

- Reboot immediately:

`shutdown -r now`

- Reboot in 5 minutes:

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` &`

- Shutdown at 1:00 pm (Uses 24h clock):

`shutdown -h 13:00`

- Cancel a pending shutdown/reboot operation:

`shutdown -c`
