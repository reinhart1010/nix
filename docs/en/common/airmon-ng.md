---
layout: page
title: common/airmon-ng (English)
description: "Activate monitor mode on wireless network devices."
content_hash: 883b3f22024c5818e807cce3e47dd9a59f888316
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/airmon-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/airmon-ng.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/airmon-ng.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/airmon-ng.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/airmon-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airmon-ng

Activate monitor mode on wireless network devices.
Part of `aircrack-ng`.
More information: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- List wireless devices and their statuses:

`sudo airmon-ng`

- Turn on monitor mode for a specific device:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Kill disturbing processes that use wireless devices:

`sudo airmon-ng check kill`

- Turn off monitor mode for a specific network interface:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
