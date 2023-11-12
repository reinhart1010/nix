---
layout: page
title: common/conda (italiano)
description: "Gestione pacchetti, dipendenze ed ambiente per qualsiasi linguaggio di programmazione."
content_hash: 9f7e8f74f53e0f204524b5e13d145bc562f46173
last_modified_at: 2023-11-12
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

`conda create --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=2.7 matplotlib</span>

- Elenca tutti gli ambienti:

`conda info --envs`

- Attiva o disattiva un ambiente:

`conda `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">activate|deactivate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>

- Elimina un ambiente rimuovendo anche tutti i pacchetti:

`conda remove --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_ambiente</span>` --all`

- Cerca un determinato pacchetto nei canali di conda:

`conda search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">package_name</span>

- Installa pacchetti nell'ambiente corrente:

`conda install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">python=3.4 numpy</span>

- Elenca i pacchetti attualmente installati nell'ambiente corrente:

`conda list`

- Elimina pacchetti inutilizzati e cache:

`conda clean --all`
