---
layout: page
title: common/git-add (Nederlands)
description: "Voegt gewijzigde bestanden toe aan de index."
content_hash: 7d8f6e1c7e7a443662620f642114e70e464bb676
last_modified_at: 2024-06-24
related_topics:
  - title: Deutsch version
    url: /de/common/git-add.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/git-add.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/git-add.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/git-add.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/git-add.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/git-add.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/git-add.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/git-add.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/git-add.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/git-add.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/git-add.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># git add

Voegt gewijzigde bestanden toe aan de index.
Meer informatie: <https://git-scm.com/docs/git-add>.

- Voeg een bestand toe aan de index:

`git add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voeg alle bestanden toe (bijgehouden en niet bijgehouden):

`git add -A`

- Voeg alle bestanden toe in de huidige map:

`git add .`

- Voeg alleen al bijgehouden bestanden toe:

`git add -u`

- Voeg ook genegeerde bestanden toe:

`git add -f`

- Interactief delen van bestanden toevoegen:

`git add -p`

- Interactief delen van een opgegeven bestand toevoegen:

`git add -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Interactief een bestand toevoegen:

`git add -i`
