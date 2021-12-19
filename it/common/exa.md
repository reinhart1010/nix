---
layout: page
title: common/exa (italiano)
description: "Un moderno sostituto per `ls` (elenca i contenuti di una directory)."
content_hash: 43854512a8e7d8ad2e17e1fc8eef2651ca358ca4
related_topics:
  - title: Deutsch version
    url: /de/common/exa.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/exa.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/exa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># exa

Un moderno sostituto per `ls` (elenca i contenuti di una directory).
Maggiori informazioni: <https://the.exa.website>.

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
