---
layout: page
title: common/aircrack-ng (Nederlands)
description: "Kraak WEP- en WPA/WPA2-sleutels van handshake in vastgelegde pakketten."
content_hash: 7c6720725c3ea522618010ed2b4c5157e03fb955
last_modified_at: 2023-07-11
related_topics:
  - title: Deutsch version
    url: /de/common/aircrack-ng.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aircrack-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aircrack-ng

Kraak WEP- en WPA/WPA2-sleutels van handshake in vastgelegde pakketten.
Onderdeel van Aircrack-ng netwerksoftwaresuite.
Meer Informatie: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Kraak-sleutel uit opnamebestand met behulp van woordenlijst:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en de essid van het toegangspunt:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en het MAC-adres van het toegangspunt:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>
