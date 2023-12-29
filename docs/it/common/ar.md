---
layout: page
title: common/ar (italiano)
description: "Crea, modifica ed estrai da archivi (`.a`, `.so`, `.o`)."
content_hash: ce70de8fcb0edcac51ba5b3160f1aa8ebded2cd0
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ar

Crea, modifica ed estrai da archivi (`.a`, `.so`, `.o`).
Maggiori informazioni: <https://manned.org/ar>.

- Estrai ([x]) tutti i membri da un archivio:

`ar x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.a</span>

- Lis[t]a tutti i membri di un archivio:

`ar t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.ar</span>

- Sostituisci ([r]) o aggiungi file ad un archvio:

`ar r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.deb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/debian-binary percorso/del/control.tar.gz percorso/del/data.tar.xz ...</span>

- In[s]erisci o sostituisci un indice in un archivio (equivalente ad usare `ranlib`):

`ar s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.a</span>

- Crea un archivio con dei file creando anche il relativo indice:

`ar rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file1.o percorso/del/file2.o ...</span>
