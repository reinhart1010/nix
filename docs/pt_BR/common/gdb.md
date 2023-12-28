---
layout: page
title: common/gdb (português (Brasil))
description: "O depurador GNU."
content_hash: 443c17da14d33b8073df83f912cbf77b90268ab3
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/gdb.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/gdb.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/gdb.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/gdb.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gdb.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gdb

O depurador GNU.
Mais informações: <https://www.gnu.org/software/gdb>.

- Depura um executável:

`gdb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável</span>

- Vincula um processo ao gdb:

`gdb -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Depura usando um arquivo de "core dump":

`gdb -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">core</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável</span>

- Executa um dado comando do gdb ao iniciar:

`gdb -ex "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comandos</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável</span>

- Inicia o gdb passando argumentos para o executável:

`gdb --args `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executável</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumento1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumento2</span>
