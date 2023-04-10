---
layout: page
title: common/assimp (italiano)
description: "Client da linea di comando per la Open Asset Import Library."
content_hash: 459d5b6e9ea89dd56cb25970f3fe60c57e650692
last_modified_at: 2023-04-10
related_topics:
  - title: English version
    url: /en/common/assimp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/assimp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/assimp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/assimp.html
    icon: bi bi-globe
---
# assimp

Client da linea di comando per la Open Asset Import Library.
Supporta il caricamento di 40+ formati di file per modelli 3D, e l'espoerazione di diversi formati 3D popolari.
Maggiori informazioni: <https://assimp-docs.readthedocs.io/>.

- Elenca tutti i formati supportati:

`assimp listext`

- Elenca tutti i formati supportati per l'esportazione:

`assimp listexport`

- Converti un file a uno dei tipi supportati, utilizzando i parametri predefiniti:

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_input.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_output.obj</span>

- Converti un file utilizzando parametri personalizzati (il file dox_cmd.h nel source code di assimp contiene una lista di parametri disponibili):

`assimp export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_input.stl</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file_output.obj</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parametri</span>

- Mostra un riepilogo del contenuto di un file:

`assimp info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file</span>

- Elenca tutti i sottocomandi disponibili (detti "verbs"):

`assimp help`

- Chiedi aiuto per uno specifico sottocomando (ad esempio riguardo i suoi parametri):

`assimp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sottocomando</span>` --help`
