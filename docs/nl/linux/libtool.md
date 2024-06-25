---
layout: page
title: linux/libtool (Nederlands)
description: "Een generiek script voor bibliotheekondersteuning dat de complexiteit van het gebruik van gedeelde bibliotheken verbergt achter een consistente, draagbare interface."
content_hash: f3d6e561b9330dbb53ba5e867ea02ed875ff985c
last_modified_at: 2024-06-25
related_topics:
  - title: English version
    url: /en/linux/libtool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/libtool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># libtool

Een generiek script voor bibliotheekondersteuning dat de complexiteit van het gebruik van gedeelde bibliotheken verbergt achter een consistente, draagbare interface.
Meer informatie: <https://www.gnu.org/software/libtool/manual/libtool.html#Invoking-libtool>.

- Compileer een bronbestand naar een `libtool`-object:

`libtool --mode=compile gcc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.c</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.lo</span>

- Maak een bibliotheek of een uitvoerbaar bestand:

`libtool --mode=link gcc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bibliotheek.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.lo</span>

- Stel automatisch het bibliotheekpad in zodat een ander programma niet-geïnstalleerde door `libtool` gegenereerde programma's of bibliotheken kan gebruiken:

`libtool --mode=execute gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/programma</span>

- Installeer een gedeelde bibliotheek:

`libtool --mode=install cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bibliotheek.la</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/installatiemap</span>

- Voltooi de installatie van `libtool`-bibliotheken op het systeem:

`libtool --mode=finish `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/installatiemap</span>

- Verwijder geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool --mode=uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/geïnstalleerde_bibliotheek.la</span>

- Verwijder niet-geïnstalleerde bibliotheken of uitvoerbare bestanden:

`libtool --mode=clean rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bron.lo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bibliotheek.la</span>
