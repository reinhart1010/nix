---
layout: page
title: common/git-blame (italiano)
description: "Mostra hash del commit ed ultimo autore per ogni riga di un file."
content_hash: 49f65371dbde0f2488955e99491603c70545cb10
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/git-blame.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-blame.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-blame.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-blame.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-blame.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-blame.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-blame.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git blame

Mostra hash del commit ed ultimo autore per ogni riga di un file.
Maggiori informazioni: <https://git-scm.com/docs/git-blame>.

- Stampa il contenuto di un file annotando ogni riga con l'hash del commit e il nome dell'autore:

`git blame `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>

- Stampa il contenuto di un file annotando ogni riga con l'hash del commit e l'indirizzo email dell'autore:

`git blame -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file</span>
