---
layout: page
title: common/calibredb (italiano)
description: "Strumentoi per gestire il tuo database di e-book."
content_hash: 813fc5205767ade1218a2bc9404df53326683d9a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/calibredb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/calibredb.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

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
