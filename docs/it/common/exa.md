---
layout: page
title: common/exa (italiano)
description: "Un moderno sostituto per `ls` (elenca i contenuti di una directory)."
content_hash: 5e2ed3065e1cecf31f011b86999f0a1f6663d5da
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/exa.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/exa.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/exa.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># exa

Un moderno sostituto per `ls` (elenca i contenuti di una directory).
Maggiori informazioni: <https://github.com/ogham/exa>.

- Elenca i file nella directory corrente, uno per riga:

`exa --oneline`

- Elenca tutti i file, inclusi quelli nascosti:

`exa --all`

- Elenca tutti i file e mostra informazioni (permessi, dimensione e data di ultima modifica):

`exa --long --all`

- Elenca i file, ordinandoli per dimensione decrescente:

`exa --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Mostra un albero dei file con 3 livelli di profondità:

`exa --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Elenca i file e mostra informazioni, ordinandoli per ultima modifica (più vechci prima):

`exa --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>
