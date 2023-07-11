---
layout: page
title: common/airdecap-ng (Nederlands)
description: "Decodeer een WEP-, WPA- of WPA2-gecodeerd opnamebestand."
content_hash: 56781f21107a647958598223f812efeec8a4d77d
last_modified_at: 2023-07-11
related_topics:
  - title: English version
    url: /en/common/airdecap-ng.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># airdecap-ng

Decodeer een WEP-, WPA- of WPA2-gecodeerd opnamebestand.
Onderdeel van Aircrack-ng netwerksoftwaresuite.
Meer Informatie: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

- Verwijder draadloze headers uit een open netwerkopnamebestand en gebruik het MAC-adres van het toegangspunt om te filteren:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Decodeer een met WEP gecodeerd opnamebestand met de sleutel in hex-indeling:

`airdecap-ng -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hex_key</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behulp van de essid en het wachtwoord van het toegangspunt:

`airdecap-ng -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behoud van de headers met behulp van de essid en het wachtwoord van het toegangspunt:

`airdecap-ng -l -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>

- Decodeer een met WPA/WPA2 gecodeerd opnamebestand met behulp van de essid en het wachtwoord van het toegangspunt en gebruik het MAC-adres om te filteren:

`airdecap-ng -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ap_mac</span>` -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">essid</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakketbestand.cap</span>
