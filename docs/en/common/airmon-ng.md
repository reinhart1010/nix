---
layout: page
title: common/airmon-ng (English)
description: "Activate monitor mode on wireless network devices."
content_hash: d123aa91c9ed919c1f81bedeea6f284cd8c18d7e
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/airmon-ng.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/airmon-ng.html
    icon: bi bi-globe
---
# airmon-ng

Activate monitor mode on wireless network devices.
More information: <https://www.aircrack-ng.org/doku.php?id=airmon-ng>.

- List wireless devices and their statuses:

`sudo airmon-ng`

- Turn on monitor mode for a specific device:

`sudo airmon-ng start `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0</span>

- Kill disturbing processes that use wireless devices:

`sudo airmon-ng check kill`

- Turn off monitor mode for a specific network interface:

`sudo airmon-ng stop `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wlan0mon</span>
