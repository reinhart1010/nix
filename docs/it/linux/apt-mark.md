---
layout: page
title: linux/apt-mark (italiano)
description: "Servizio per cambiare lo stato di un pacchetto installato."
content_hash: ed80bda94cf1e923db97104440fb5dafa300068d
related_topics:
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
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-mark.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-mark.html
    icon: bi bi-globe
---
# apt-mark

Servizio per cambiare lo stato di un pacchetto installato.
Maggiori informazioni: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

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
