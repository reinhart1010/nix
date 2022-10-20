---
layout: page
title: common/fmt (italiano)
description: "Riformatta i paragrafi di un file di testo unendoli e limitando la larghezza delle righe a un dato numero di caratteri (di default 75)."
content_hash: 9655416c7c85282da37845442bb55117e567103b
related_topics:
  - title: English version
    url: /en/common/fmt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fmt.html
    icon: bi bi-globe
---
# fmt

Riformatta i paragrafi di un file di testo unendoli e limitando la larghezza delle righe a un dato numero di caratteri (di default 75).
Maggiori informazioni: <https://www.gnu.org/software/coreutils/fmt>.

- Riformatta un file:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riformatta un file producendo linee di (al massimo) `n` caratteri:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riformatta un file senza unire assieme le linee più corte della data larghezza:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Riformatta un file usando una spaziatura uniforme (1 spazio tra due parole e 2 spazi tra due paragrafi):

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>
