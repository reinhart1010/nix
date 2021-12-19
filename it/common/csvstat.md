---
layout: page
title: common/csvstat (italiano)
description: "Stampa statistiche descrittive per tutte le colonne di un file CSV."
content_hash: 2593fb94476b5adc5bed82c7445ee9f278dc5d5a
related_topics:
  - title: English version
    url: /en/common/csvstat.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/csvstat.html
    icon: bi bi-globe
---
# csvstat

Stampa statistiche descrittive per tutte le colonne di un file CSV.
Incluso in csvkit.
Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvstat.html>.

- Mostra tutte le statistiche per tutte le colonne:

`csvstat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Mostra tutte le statistiche per le colonne 2 e 4:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2,4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Mostra la somma per tutte le colonne:

`csvstat --sum `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Mostra la lunghezza massima dei valori della colonna 3:

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` --len `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>

- Mostra il numedo di valori unici nella colonna "nome":

`csvstat -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dati.csv</span>
