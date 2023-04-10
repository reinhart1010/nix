---
layout: page
title: common/aircrack-ng (Deutsch)
description: "WEP und WPA/WPA2 Schlüssel im Kommunikationsaufbau knacken."
content_hash: ad28e2f775a3fc9b510d4eb14ad59bf04c7ba4ef
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/aircrack-ng.html
    icon: bi bi-globe
---
# aircrack-ng

WEP und WPA/WPA2 Schlüssel im Kommunikationsaufbau knacken.
Teil des Aircrack-ng Softwarepakets.
Weitere Informationen: <https://www.aircrack-ng.org/doku.php?id=aircrack-ng>.

- Knacke Schlüssel von abgefangenen Paketen mithilfe von Wortlisten:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/wortliste.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/packetdatei.cap</span>

- Knacke Schlüssel von abgefangenen Paketen mithilfe einer Wortliste und der (E)SSID des Access Points:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/wortliste.txt</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/packetdatei.cap</span>

- Knacke Schlüssel von abgefangenen Paketen mithilfe einer Wortliste und der MAC-Adresse des Access Points:

`aircrack-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/wortliste.txt</span>` --bssid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/packetdatei.cap</span>
