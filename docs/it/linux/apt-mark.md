---
layout: page
title: linux/apt-mark (italiano)
description: "Servizio per cambiare lo stato di un pacchetto installato."
content_hash: 9bb5c7f5e578717079b3bb53c8b8c0354959fe53
last_modified_at: 2024-09-18
related_topics:
  - title: català version
    url: /ca/linux/apt-mark.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-mark.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-mark.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-mark.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-mark.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-mark.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-mark

Servizio per cambiare lo stato di un pacchetto installato.
Maggiori informazioni: <https://manned.org/apt-mark.8>.

- Contrassegna un pacchetto come installato automaticamente:

`sudo apt-mark auto `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Mantiene un pacchetto alla sua versione attuale e ne previene l'aggiornamento:

`sudo apt-mark hold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Consente ad un pacchetto di essere nuovamente aggiornato:

`sudo apt-mark unhold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_del_pacchetto</span>

- Mostra i pacchetti installati manualmente:

`apt-mark showmanual`

- Visualizza i pacchetti mantenuti alla versione attuale che non sono stati aggiornati:

`apt-mark showhold`
