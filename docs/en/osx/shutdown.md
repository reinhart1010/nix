---
layout: page
title: osx/shutdown (English)
description: "Shutdown and reboot the system."
content_hash: c6017c45c8f3590357ef43242cddf509a575429c
last_modified_at: 2024-01-31
related_topics:
  - title: 中文 version
    url: /zh/osx/shutdown.html
    icon: bi bi-globe
tldri18n_status: 2
---
# shutdown

Shutdown and reboot the system.
More information: <https://keith.github.io/xcode-man-pages/shutdown.8.html>.

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
