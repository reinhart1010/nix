---
layout: page
title: osx/shutdown (English)
description: "Shutdown and reboot the system."
content_hash: dd6366013685746da88c80f9426a05a12ed9f88f
related_topics:
  - title: 中文 version
    url: /zh/osx/shutdown.html
    icon: bi bi-globe
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

`shutdown -r +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Power off (halt) at 1:00 pm (Uses 24h clock):

`shutdown -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1300</span>

- Reboot on May 10th 2042 at 11:30 am (Input format: YYMMDDHHMM):

`shutdown -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4205101130</span>
