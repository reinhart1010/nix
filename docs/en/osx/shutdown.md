---
layout: page
title: osx/shutdown (English)
description: "Shutdown and reboot the system."
content_hash: 04fac018f730141d122f806370e15e82bbb50e57
last_modified_at: 2023-11-12
related_topics:
  - title: 中文 version
    url: /zh/osx/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

Shutdown and reboot the system.
More information: <https://ss64.com/osx/shutdown.html>.

- Power off (halt) immediately:

`shutdown -h now`

- Sleep immediately:

`shutdown -s now`

- Reboot immediately:

`shutdown -r now`

- Reboot in 5 minutes:

`shutdown -r "+`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>`"`

- Power off (halt) at 1:00 pm (Uses 24h clock):

`shutdown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1300</span>

- Reboot on May 10th 2042 at 11:30 am (Input format: YYMMDDHHMM):

`shutdown -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4205101130</span>
