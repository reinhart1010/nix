---
layout: page
title: common/aircrack-ng (Nederlands)
description: "Kraak WEP- en WPA/WPA2-sleutels van handshake in vastgelegde pakketten."
content_hash: fd35391e87739f33366f6a146ff70353252e1367
last_modified_at: 2023-11-06
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
# aircrack-ng

Kraak WEP- en WPA/WPA2-sleutels van handshake in vastgelegde pakketten.
Onderdeel van Aircrack-ng netwerksoftwaresuite.
Meer informatie: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Kraak-sleutel uit opnamebestand met behulp van woordenlijst:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en de essid van het toegangspunt:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Kraak de sleutel uit het opnamebestand met behulp van de woordenlijst en het MAC-adres van het toegangspunt:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/woordenlijst.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>
