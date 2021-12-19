---
layout: page
title: common/git-show (italiano)
description: "Mostra vari tipi di oggetti Git (commit, tag, etc.)."
content_hash: 3083afe91b8a883a165194c8240b6f93dc74be9b
related_topics:
  - title: English version
    url: /en/common/git-show.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-show.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-show.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-show.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git show

Mostra vari tipi di oggetti Git (commit, tag, etc.).
Maggiori informazioni: <https://git-scm.com/docs/git-show>.

- Mostra informazioni sull'ultimo commit (hash, messaggio, modifiche, ed altri metadati):

`git show`

- Mostra informazioni su un dato commit:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Mostra informazioni sul commit associato ad un tag specifico:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Mostra informazioni sul terzo commit dalla cima del ramo:

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ramo</span>`~`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Mostra il messaggio di commit su linea singola, senza mostrare il diff:

`git show --oneline -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Mostra solo la lista dei file modificati in un commit:

`git show --stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commit</span>

- Mostra il contenuto di un file ad una data revisione (ad esempio, in un ramo, tag o commit):

`git show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revisione</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>
