---
layout: page
title: linux/adduser (italiano)
description: "Servizio per aggiungere utenti."
content_hash: 9d35c78bae77f37e14a0e48e894a859a5ca2e89f
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
  - title: suomi version
    url: /fi/linux/adduser.html
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
  - title: português (Brasil) version
    url: /pt_BR/linux/adduser.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/adduser.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/adduser.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># adduser

Servizio per aggiungere utenti.
Maggiori informazioni: <https://manned.org/adduser>.

- Crea un nuovo utente con una directory home predefinita e richiede all'utente di impostare una password:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>

- Crea un utente senza una directory home:

`adduser --no-create-home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>

- Crea un utente con una directory home nel percorso specificato:

`adduser --home `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/home</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>

- Crea un nuovo utente con l'interprete di comandi(shell) specificato come shell di accesso:

`adduser --shell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>

- Crea un nuovo utente appartenente al gruppo specificato:

`adduser --ingroup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>

- Aggiunge un utente esistente al gruppo specificato:

`adduser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_utente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppo</span>
