---
layout: page
title: common/git-bundle (italiano)
description: "Colloca oggetti e riferimenti in un archivio."
content_hash: 4a057daac32a0aef873459909f1c63570c6be143
last_modified_at: 2024-08-15
related_topics:
  - title: English version
    url: /en/common/git-bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-bundle.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-bundle.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-bundle.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-bundle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git bundle

Colloca oggetti e riferimenti in un archivio.
Maggiori informazioni: <https://git-scm.com/docs/git-bundle>.

- Crea un file bundle che contiene tutti gli oggetti e riferimenti di un dato ramo:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>

- Crea un file bundle di tutti i rami:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>` --all`

- Crea un file bundle degli ultimi 5 commit sul ramo corrente:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>` -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Crea un file bundle degli ultimi 7 giorni:

`git bundle create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>` --since=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">7.days</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HEAD</span>

- Verifica che un file bundle sia valido e possa essere applicato al repository in uso:

`git bundle verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>

- Stampa su standard output la lista di riferimenti contenuti in un bundle:

`git bundle unbundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>

- Dato un file bundle, estrai un ramo specifico nel repository in uso:

`git pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.bundle</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ramo</span>
