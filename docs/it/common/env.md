---
layout: page
title: common/env (italiano)
description: "Mostra le variabili d'ambiente o esegui un programma in un ambiente modificato."
content_hash: 7e35ccf1111ff62ceb94a8e2b9f2fe74df390bfc
related_topics:
  - title: English version
    url: /en/common/env.html
    icon: bi bi-globe
  - title: norsk bokmål (Norge) version
    url: /no/common/env.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/env.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># env

Mostra le variabili d'ambiente o esegui un programma in un ambiente modificato.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/env>.

- Mostra le variabili d'ambiente:

`env`

- Esegui un programma. Utilizzato spesso in script dopo lo shebang (#!) per cercare il percorso del programma:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Resetta l'ambiente ed esegui un programma:

`env -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Rimuovi una variabile dall'ambiente ed esegui un programma:

`env -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>

- Setta una variabile ed esegui un programma:

`env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">variabile</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valore</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma</span>
