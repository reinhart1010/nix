---
layout: page
title: linux/cp (italiano)
description: "Copia file e directory."
content_hash: 1d8f859604e39dff00b075ff155444ab5c8e6a41
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/cp.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/cp.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cp.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/cp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/cp.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/cp.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/cp.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/cp.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/cp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/cp.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/linux/cp.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># cp

Copia file e directory.
Maggiori informazioni: <https://www.gnu.org/software/coreutils/cp>.

- Copia un file in un'altra posizione:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_da_copiare.est</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_di_destinazione.est</span>

- Copia un file all'interno di una directory, mantenendone uguale il nome:

`cp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_da_copiare.est</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory</span>

- Copia ricorsivamente i contenuti di una directory in un'altra posizione (se la destinazione esiste, la directory è copiata al suo interno):

`cp -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_da_copiare</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/di/destinazione</span>

- Copia una directory ricorsivamente in modalità prolissa (mostra i file mentre vengono copiati):

`cp -vr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/directory_da_copiare</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/di/destinazione</span>

- Copia i file di testo in un'altra posizione, in modalità interattiva (richiede conferma all'utente prima di sovrascrivere):

`cp -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/di/destinazione</span>

- Segue i collegamenti simbolici prima di copiare:

`cp -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">collegamento</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/di/destinazione</span>

- Utilizza il percorso completo dei file originali, creando ogni directory intermedia mancante mentre durante la copia:

`cp --parents `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/dei/file/da/copiare</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file/destinazione</span>
