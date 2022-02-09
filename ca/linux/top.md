---
layout: page
title: linux/top (català)
description: "Mostra informació dinàmica en temps real sobre processos executant-se."
content_hash: 5d989879510abc06e35015309315b517e5609070
related_topics:
  - title: English version
    url: /en/linux/top.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/top.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/top.html
    icon: bi bi-globe
---
# top

Mostra informació dinàmica en temps real sobre processos executant-se.
Més informació: <https://manned.org/top>.

- Inicia top:

`top`

- No mostra cap procés inactiu o zombie:

`top -i`

- Mostra només processos pertanyents a un usari donat:

`top -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuari</span>

- Ordena processos per una columna:

`top -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_columna</span>

- Mostra els fils individuals d'un procés donat:

`top -Hp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_procés</span>

- Mostra només els processos amb un(s) PID(s) donat(s), separats per comes. (Normalment no es coneix el PID amb antelació. Aquest exemple l'obté del nom del procés):

`top -p $(pgrep -d ',' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_procés</span>`)`

- Obté ajuda sobre els commandaments interactius:

`?`
