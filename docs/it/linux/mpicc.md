---
layout: page
title: linux/mpicc (italiano)
description: "Involucro Open MPI per il compilatore di C."
content_hash: 908f3f3978fc478434d0165e30afdb352e42a7c3
last_modified_at: 2023-04-13
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mpicc

Involucro Open MPI per il compilatore di C.
Shell che esegue sul compilatore, aggiungono i relevanti argomenti e linkers necessari a compilare/collegare programmi Open MPI, invocando il sottostante compilatore di C per effettuare le effetive operazioni.
Maggiori informazioni: <https://www.mpich.org/static/docs/latest/www1/mpicc.html>.

- Compila un file sorgente in un file oggetto:

`mpicc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.c</span>

- Linka un file oggetto file e genera un eseguibile:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.o</span>

- Linka e compila i file sorgente in un solo commando:

`mpicc -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">executable</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.c</span>
