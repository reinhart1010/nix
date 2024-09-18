---
layout: page
title: linux/adduser (suomi)
description: "Käyttäjän lisäysapuohjelma."
content_hash: 67c2b8f251ea991e349bdee52748ad4f87533fb4
last_modified_at: 2024-09-18
related_topics:
  - title: Deutsch version
    url: /de/linux/adduser.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/adduser.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/adduser.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/adduser.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/adduser.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/adduser.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 2
---
# adduser

Käyttäjän lisäysapuohjelma.
Lisätietoja: <https://manned.org/adduser>.

- Luo uusi käyttäjä oletuskotihakemistolla ja pyydä käyttäjää asettamaan salasana:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tunnus</span>

- Luo uusi käyttäjä ilman kotihakemistoa:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tunnus</span>

- Luo uusi käyttäjä kotihakemistolla määritetyssä polussa:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">polku/kotiin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tunnus</span>

- Luo uusi käyttäjä, jolla on määritetty kuori kirjautumiskuoreksi:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">polku/kuoriin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tunnus</span>

- Luo uusi käyttäjä, joka kuuluu määritettyyn ryhmään:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ryhmä</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tunnus</span>
