---
layout: page
title: common/calibredb (italiano)
description: "Strumentoi per gestire il tuo database di e-book."
content_hash: 813fc5205767ade1218a2bc9404df53326683d9a
related_topics:
  - title: English version
    url: /en/common/calibredb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibredb.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/calibredb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># calibredb

Strumentoi per gestire il tuo database di e-book.
Parte del manager di e-book Calibre.
Maggiori informazioni: <https://manual.calibre-ebook.com/generated/en/calibredb.html>.

- Elenca gli e-book nella libreria con informazioni aggiuntive:

`calibredb list`

- Cerca tra gli e-book mostrando informazioni aggiuntive:

`calibredb list --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termine_di_ricerca</span>

- Cerca mostrando solamente gli ID degli e-book:

`calibredb search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">termine_di_ricerca</span>

- Aggiungi uno o più e-book alla libreria:

`calibredb add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1 file2 …</span>

- Rimuovi uno o più e-book dalla libreria. Sono necessari gli ID (vedi sopra):

`calibredb remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id1 id2 …</span>
