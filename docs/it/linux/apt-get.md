---
layout: page
title: linux/apt-get (italiano)
description: "Servizio di gestione dei pacchetti per Debian e Ubuntu."
content_hash: 71a7bd715ba38fe7e3beccf6b02d97a160a3390f
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Servizio di gestione dei pacchetti per Debian e Ubuntu.
Cerca i pacchetti usando `apt-cache`.
Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Aggiorna la lista dei pacchetti e delle loro versioni disponibili (è consigliato eseguire questo comando prima di altri comandi `apt-get`):

`apt-get update`

- Installa un pacchetto, o lo aggiorna all'ultima versione disponibile:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Rimuove un pacchetto:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Rimuove un pacchetto ed i suoi file di configurazione:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pacchetto</span>

- Aggiorna tutti i pacchetti installati alla versione disponibile più recente:

`apt-get upgrade`

- Pulisce gli archivi locali - rimuovendo i file (.deb) da scaricamenti interrotti che non possono più essere scaricati:

`apt-get autoclean`

- Rimuove tutti i pacchetti che non sono più necessari:

`apt-get autoremove`

- Aggiorna tutti i pacchetti installati (come `upgrade`), rimuovendo i pacchetti obsoleti ed installando ulteriori pacchetti per soddisfare le nuove dipendenze:

`apt-get dist-upgrade`
