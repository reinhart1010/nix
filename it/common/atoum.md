---
layout: page
title: common/atoum (italiano)
description: "Un semplice, moderno ed intuitivo framework PHP per unit testing."
content_hash: 6e4c034d72e7c686bb8ac433ed306f620c0ab09c
related_topics:
  - title: English version
    url: /en/common/atoum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atoum.html
    icon: bi bi-globe
---
# atoum

Un semplice, moderno ed intuitivo framework PHP per unit testing.
Maggiori informazioni: <http://atoum.org>.

- Inizializza un file di configurazione:

`atoum --init`

- Esegui tutti i test:

`atoum`

- Esegui test utilizzando uno specifico file di configurazione:

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Esegui uno specifico file di test:

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>

- Esegui una specifica directory di test:

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Esegui tutti i test sotto uno specifico namespace:

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Esegui tutti i test con uno speficico tag:

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Carica un file di bootstrap personalizzato prima di eseguire i test:

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">percorso/al/file</span>
