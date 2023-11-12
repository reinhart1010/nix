---
layout: page
title: common/comm (italiano)
description: "Seleziona o ignora linee comuni a due file. Entrambi i file devono essere ordinati."
content_hash: 3ed462f51dc500d9a6ce385b6908bf183f41da56
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/comm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/comm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comm

Seleziona o ignora linee comuni a due file. Entrambi i file devono essere ordinati.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/comm>.

- Produci tre colonne separate da tab: linee solo nel primo file, linee solo nel secondo file, e linee comuni ad entrambi:

`comm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Stampa solo le linee comune ad entrambi i file:

`comm -12 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Stampa solo le lin comuni ad entrambi i file, leggendone uno da standard input:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` | comm -12 - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>

- Filtra le linee trovate solo nel primo file, salvando il risultato in un terzo file:

`comm -23 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file3</span>

- Filtra le linee trovate solo nel secondo file, con due file che non sono ordinati:

`comm -13 <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file1</span>`) <(sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file2</span>`)`
