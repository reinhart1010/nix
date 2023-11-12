---
layout: page
title: common/awk (italiano)
description: "Un versatile linguaggio di programmazione per elaborare file."
content_hash: e02f17c720f4f89e62232774c9f13cdc153d8dec
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/awk.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/awk.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/awk.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/awk.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/awk.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/awk.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/awk.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/awk.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># awk

Un versatile linguaggio di programmazione per elaborare file.
Maggiori informazioni: <https://github.com/onetrueawk/awk>.

- Stampa la quinta colonna (field) in un file di linee separate da spazi:

`awk '{print $5}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Stampa la seconda colonna delle linee contenenti "qualcosa":

`awk '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">qualcosa</span>`/ {print $2}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Stampa l'ultima colonna di ogni linea di un file, utilizzando la virgola (invece dello spazio) come separatore di colonne:

`awk -F ',' '{print $NF}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Somma i valori nella prima colonna di un file e stampa il totale:

`awk '{s+=$1} END {print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Somma i valori nella prima colonna e stampali seguiti dal totale:

`awk '{s+=$1; print $1} END {print "--------"; print s}' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>

- Stampa una liena ogni tre iniziando dalla prima:

`awk 'NR%3==1' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_file</span>
