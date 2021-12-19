---
layout: page
title: common/box (italiano)
description: "Una applicazione PHP per creare e gestire Phars."
content_hash: 5f8b6f237f4a9e75f0c8d4def5fd425810074a89
related_topics:
  - title: English version
    url: /en/common/box.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/box.html
    icon: bi bi-globe
---
# box

Una applicazione PHP per creare e gestire Phars.
Maggiori informazioni: <https://github.com/box-project/box>.

- Crea un nuovo file Phar:

`box build`

- Crea un nuovo file Phar usando uno specifico file di configurazione:

`box build -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/configurazione</span>

- Mostra informazioni sulla estensione PHP PHAR:

`box info`

- Mostra informazioni su di uno specifico file Phar:

`box info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_phar</span>

- Valida il primo file di configurazione trovato nella directory corrente:

`box validate`

- Verifica la firma di uno specifico file Phar:

`box verify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/a/file_phar</span>

- Mostra tutti i comandi ed opzioni disponibili:

`box help`
