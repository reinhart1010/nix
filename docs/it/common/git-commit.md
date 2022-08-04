---
layout: page
title: common/git-commit (italiano)
description: "Salva file nell'area di stage in una nuova istantanea del tuo repository."
content_hash: 2fc51448ab0d1e415c9890367014803434e4d564
related_topics:
  - title: Deutsch version
    url: /de/common/git-commit.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-commit.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-commit.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-commit.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-commit.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-commit.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-commit.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/git-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># git commit

Salva file nell'area di stage in una nuova istantanea del tuo repository.
Maggiori informazioni: <https://git-scm.com/docs/git-commit>.

- Committa sul repository i file nell'area di stage con un messaggio:

`git commit -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>`"`

- Aggiungi all'area di stage tutti i file modificati e committali con un messaggio:

`git commit -a -m "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messaggio</span>`"`

- Sostituisci l'ultimo commit con le modifiche attualmente salvate nell'area di stage:

`git commit --amend`

- Committa solo i file specificati (tra quelli presenti nell'area di stage):

`git commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file2</span>
