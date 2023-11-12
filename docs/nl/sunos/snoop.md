---
layout: page
title: sunos/snoop (Nederlands)
description: "Network packet sniffer."
content_hash: e6a5bee0c7a7671d6c291719d49443ad12608ea9
last_modified_at: 2023-11-12
related_topics:
  - title: বাংলা version
    url: /bn/sunos/snoop.html
    icon: bi bi-globe
  - title: English version
    url: /en/sunos/snoop.html
    icon: bi bi-globe
  - title: français version
    url: /fr/sunos/snoop.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/sunos/snoop.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/sunos/snoop.html
    icon: bi bi-globe
tldri18n_status: 2
---
# snoop

Network packet sniffer.
SunOS equivalent van tcpdump.
Meer informatie: <https://www.unix.com/man-page/sunos/1m/snoop>.

- Capteer de pakketten van een specifieke netwerk interface:

`snoop -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">e1000g0</span>

- Slaag de pakketten op in een bestand, in plaats van ze weer te geven:

`snoop -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Toon de verboze protocal layer samenvatting van de pakketten in een bestand:

`snoop -V -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Capteren van netwerk pakketten die van een bepaalde host komen en naar een gegeven poort gaan:

`snoop to port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` from host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostnaam</span>

- Capteren en weergave van een hex-dump van network pakketten die uitgewisseld zijn tussen twee IP addressen:

`snoop -x0 -p4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres_2</span>
