---
layout: page
title: common/airdecap-ng (Nederlands)
description: "Decodeer een WEP-, WPA- of WPA2-gecodeerd opnamebestand."
content_hash: f1466f1b48e76aa89259258132190be2887b590f
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/airdecap-ng.html
    icon: bi bi-globe
tldri18n_status: 2
---
# airdecap-ng

Decodeer een WEP-, WPA- of WPA2-gecodeerd opnamebestand.
Onderdeel van Aircrack-ng netwerksoftwaresuite.
Meer informatie: <https://www.aircrack-ng.org/doku.php?id=airdecap-ng>.

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
