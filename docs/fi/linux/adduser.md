---
layout: page
title: linux/adduser (suomi)
description: "Käyttäjän lisäysapuohjelma."
content_hash: fe682fe9be32e4f191a1c513f4367be168b704db
last_modified_at: 2023-10-27
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
  - title: italiano version
    url: /it/linux/adduser.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
---
# adduser

Käyttäjän lisäysapuohjelma.
Lisätietoja: <https://manpages.debian.org/latest/adduser/adduser.html>.

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
