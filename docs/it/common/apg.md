---
layout: page
title: common/apg (italiano)
description: "Crea password randomiche arbitrariamente complesse."
content_hash: 631905ef9789eae800004a0c49187b0e9e18357c
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/apg.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/apg.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/apg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/apg.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/apg.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/apg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apg

Crea password randomiche arbitrariamente complesse.
Maggiori informazioni: <https://manned.org/apg>.

- Genera password randomiche (la lunghezza predefinita è 8):

`apg`

- Crea una password con almeno 1 simbolo (S), 1 numero (N), 1 lettera maiuscola (C) e una minuscola (L):

`apg -M SNCL`

- Crea una password di 16 caratteri:

`apg -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crea una password di massimo 16 caratteri:

`apg -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- Crea una password che non è già presente in un dizionario (file dizionario fornito come argomento):

`apg -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/dizionario</span>
