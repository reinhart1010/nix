---
layout: page
title: linux/apt (italiano)
description: "Servizio di gestione dei pacchetti per distribuzioni basate su Debian."
content_hash: d9c64711fe5430b662327ea3ad66366195c36a2d
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Servizio di gestione dei pacchetti per distribuzioni basate su Debian.
Rimpiazzo raccomandato di `apt-get` quando usato interattivamente su Ubuntu 16.04 e versioni successive.
Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Aggiorna la lista dei pacchetti e delle loro versioni disponibili (è consigliato eseguire questo comando prima di altri comandi `apt`):

`sudo apt update`

- Cerca per un dato pacchetto:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Mostra le informazioni su un pacchetto:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Installa un pacchetto, o lo aggiorna all'ultima versione disponibile:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Rimuove un pacchetto (usando `purge` rimuove anche i suoi file di configurazione):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Aggiorna tutti i pacchetti installati alla versione disponibile più recente:

`sudo apt upgrade`

- Elenca tutti i pacchetti:

`apt list`

- Elenca i pacchetti installati:

`apt list --installed`
