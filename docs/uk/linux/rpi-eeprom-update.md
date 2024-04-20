---
layout: page
title: linux/rpi-eeprom-update (українська)
description: "Оновити EEPROM та переглянути іншу інформацію про EEPROM."
content_hash: 00401f63709cb997846a4df97a5c9dc6fe11c876
last_modified_at: 2024-04-20
related_topics:
  - title: English version
    url: /en/linux/rpi-eeprom-update.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rpi-eeprom-update.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rpi-eeprom-update

Оновити EEPROM та переглянути іншу інформацію про EEPROM.
Більше інформації: <https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#rpi-eeprom-update>.

- Переглянути інформацію про поточний встановлений EEPROM raspberry pi:

`sudo rpi-eeprom-update`

- Оновити Raspberry Pi EEPROM:

`sudo rpi-eeprom-update -a`

- Скасувати незавершене оновлення:

`sudo rpi-eeprom-update -r`

- Показати довідку:

`rpi-eeprom-update -h`
