---
layout: page
title: linux/rm (Nederlands)
description: "Verwijder bestanden of directories."
content_hash: c480c75b64dd5ed5c1804e40fed4f09aec110cec
last_modified_at: 2025-01-03
related_topics:
  - title: العربية version
    url: /ar/linux/rm.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/rm.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/rm.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rm

Verwijder bestanden of directories.
Bekijk ook: `rmdir`.
Meer informatie: <https://www.gnu.org/software/coreutils/rm>.

- Verwijder specifieke bestanden:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Verwijder specifieke bestanden waarbij niet-bestaande genegeerd worden:

`rm --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Verwijder specifieke bestanden interactief met een prompt voor elke verwijdering:

`rm --interactive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Verwijder specifieke bestanden met het afdrukken van informatie over elke verwijdering:

`rm --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Verwijder specifieke bestanden en directories recursief:

`rm --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Verwijder lege directories (dit wordt beschouwd als de veilige methode):

`rm --dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>
