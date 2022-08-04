---
layout: page
title: common/neofetch (italiano)
description: "Strumento CLI per visualizzare informazioni al OS, software e hardware."
content_hash: 0aba8ff2d463012492f4d18e959dd96673ff17d3
related_topics:
  - title: English version
    url: /en/common/neofetch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/neofetch.html
    icon: bi bi-globe
---
# neofetch

Strumento CLI per visualizzare informazioni al OS, software e hardware.
Maggiori informazioni: <https://github.com/dylanaraps/neofetch>.

- Stampa secondo la configurazione predefinita e genera una configurazione, se è la prima volta:

`neofetch`

- Attiva o disattiva la visualizzazione di una riga di informazioni nell'output, dove 'infoname' è il nome della funzione nel config, e.g. 'memory':

`neofetch --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">enable|disable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">infoname</span>

- Nascondi/mostri l'architettura del OS:

`neofetch --os_arch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>

- Attiva/disattiva marca CPU nell' output:

`neofetch --cpu_brand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">on|off</span>
