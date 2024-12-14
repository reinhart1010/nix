---
layout: page
title: common/comm (italiano)
description: "Seleziona o ignora linee comuni a due file. Entrambi i file devono essere ordinati."
content_hash: 13d29c47c001b0ea60dfc87ad79730030cd2e26c
last_modified_at: 2024-12-14
related_topics:
  - title: English version
    url: /en/common/comm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/comm.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/comm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# comm

Seleziona o ignora linee comuni a due file. Entrambi i file devono essere ordinati.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

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
