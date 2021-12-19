---
layout: page
title: osx/as (italiano)
description: "Assembler GNU portabile."
content_hash: 7e675a993f2d463524133fb4789d5f629407a919
related_topics:
  - title: English version
    url: /en/osx/as.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/as.html
    icon: bi bi-globe
---
# as

Assembler GNU portabile.
Progettato principalmente per assemblare l'output di `gcc` ed utilizzarlo con `ld`.
Maggiori informazioni: <https://www.unix.com/man-page/osx/1/as/>.

- Assembla un file, scrivendo l'output su a.out:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>

- Assembla l'output nel file dato:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">out.o</span>

- Genera l'output più velocemente saltando gli spazi e senza preprocessare i commenti. (Questo comando dovrebbe essere utilizzato solo con compilatori fidati):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>

- Includi un percorso dato alla lista delle cartelle in cui cercare i file specificati nelle direttive `.include`:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.s</span>
