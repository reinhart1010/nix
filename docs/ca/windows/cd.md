---
layout: page
title: windows/cd (català)
description: "Mostra el directori actual o canvia a un directori diferent."
content_hash: 5a716dbc0d706ae86ccdc0cc06fc02b10e693cd2
last_modified_at: 2024-10-28
related_topics:
  - title: বাংলা version
    url: /bn/windows/cd.html
    icon: bi bi-globe
  - title: čeština version
    url: /cs/windows/cd.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/windows/cd.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/cd.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/cd.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/cd.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/windows/cd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/windows/cd.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/windows/cd.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/cd.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/cd.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/windows/cd.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cd.html
    icon: bi bi-globe
  - title: ไทย version
    url: /th/windows/cd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cd

Mostra el directori actual o canvia a un directori diferent.
En PowerShell, aquesta ordre és an àlies de `Set-Location`. Aquesta documentació està basada en la versió Command Prompt (`cmd`) de `cd`.
Més informació: <https://learn.microsoft.com/windows-server/administration/windows-commands/cd>.

- Mostra documentació de l'ordre PowerShell equivalent:

`tldr set-location`

- Mostra la ruta (path) del directori actual:

`cd`

- Canvia a un directori específic en el mateix disc:

`cd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directori</span>

- Canvia a un directori específic en un altre [d]isc:

`cd /d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">C</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta\al\directori</span>

- Canvia al directori superior:

`cd ..`

- Canvia al directori inicial de l'usuari actual:

`cd %userprofile%`

- Canvia a l'arrel de la unitat actual:

`cd \`
