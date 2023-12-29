---
layout: page
title: common/box (italiano)
description: "Una applicazione PHP per creare e gestire Phars."
content_hash: 54ad5ba7bb7937b3af08b832d0891993f04dbf5a
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/box.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/box.html
    icon: bi bi-globe
tldri18n_status: 2
---
# box

Una applicazione PHP per creare e gestire Phars.
Maggiori informazioni: <https://github.com/box-project/box>.

- Crea un nuovo file Phar:

`box compile`

- Crea un nuovo file Phar usando uno specifico file di configurazione:

`box compile -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/della/configurazione</span>

- Mostra informazioni sulla estensione PHP PHAR:

`box info`

- Mostra informazioni su di uno specifico file Phar:

`box info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_phar</span>

- Valida il primo file di configurazione trovato nella directory corrente:

`box validate`

- Verifica la firma di uno specifico file Phar:

`box verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/del/file_phar</span>

- Mostra tutti i comandi ed opzioni disponibili:

`box help`
