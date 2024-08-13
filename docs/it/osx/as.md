---
layout: page
title: osx/as (italiano)
description: "Assembler GNU portabile."
content_hash: c8879184bb286ba6570adb6440d4e9e062b73c1e
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Assembler GNU portabile.
Progettato principalmente per assemblare l'output di `gcc` ed utilizzarlo con `ld`.
Maggiori informazioni: <https://keith.github.io/xcode-man-pages/as.1.html>.

- Assembla un file, scrivendo l'output su a.out:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.s</span>

- Assembla l'output nel file dato:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/out.o</span>

- Genera l'output più velocemente saltando gli spazi e senza preprocessare i commenti. (Questo comando dovrebbe essere utilizzato solo con compilatori fidati):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.s</span>

- Includi un percorso dato alla lista delle directory in cui cercare i file specificati nelle direttive `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.s</span>
