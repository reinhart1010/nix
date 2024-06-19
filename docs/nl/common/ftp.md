---
layout: page
title: common/ftp (Nederlands)
description: "Hulpmiddelen om via het File Transfer Protocol met een server te communiceren."
content_hash: 1e5a7e42b443309ca33ee64589993f016bc1e3f6
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/ftp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ftp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ftp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ftp

Hulpmiddelen om via het File Transfer Protocol met een server te communiceren.
Meer informatie: <https://manned.org/ftp>.

- Verbinden met een FTP-server:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp.voorbeeld.com</span>

- Verbinden met een FTP-server met opgave van IP-adres en poort:

`ftp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_adres</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Omschakelen naar binaire overdrachtsmodus (grafische bestanden, gecomprimeerde bestanden, etc):

`binary`

- Meerdere bestanden overdragen zonder bevestiging voor elk bestand:

`prompt off`

- Meerdere bestanden downloaden (glob-expressie):

`mget `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- Meerdere bestanden uploaden (glob-expressie):

`mput `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.zip</span>

- Meerdere bestanden verwijderen op de externe server:

`mdelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- Een bestand hernoemen op de externe server:

`rename `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">originele_bestandsnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_bestandsnaam</span>
