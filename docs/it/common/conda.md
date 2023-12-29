---
layout: page
title: common/conda (italiano)
description: "Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione."
content_hash: 28fc53b3ffcb484b6f820a1da0f7163100ccbc26
last_modified_at: 2023-12-29
related_topics:
  - title: Deutsch version
    url: /de/common/conda.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/conda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/conda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conda

Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione.
Alcuni comandi aggiuntivi, come `conda create`, hanno la propria documentazione.
Maggiori informazioni: <https://github.com/conda/conda>.

- Crea un nuovo ambiente, installandovi alcuni pacchetti:

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.9 matplotlib</span>

- Elenca tutti gli ambienti:

`conda info --envs`

- Attiva un ambiente:

`conda activate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>

- Disattiva un ambiente:

`conda deactivate`

- Elimina un ambiente rimuovendo anche tutti i pacchetti:

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>` --all`

- Installa pacchetti nell'ambiente corrente:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- Elenca i pacchetti attualmente installati nell'ambiente corrente:

`conda list`

- Elimina pacchetti inutilizzati e cache:

`conda clean --all`
