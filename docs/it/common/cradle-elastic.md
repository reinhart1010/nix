---
layout: page
title: common/cradle-elastic (italiano)
description: "Gestisci le istanze ElasticSearch per un'istanza Cradle."
content_hash: ea52ab8b882216b95870e8aacc334e9e1be1675b
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-elastic.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-elastic.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-elastic.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cradle elastic

Gestisci le istanze ElasticSearch per un'istanza Cradle.
Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#elastic>.

- Svuota l'indice ElasticSearch:

`cradle elastic flush`

- Svuota l'indice ElasticSearch per uno specifico pacchetto:

`cradle elastic flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Carica lo schema ElasticSearch:

`cradle elastic map`

- Carica lo schema ElasticSearch per uno specifico pacchetto:

`cradle elastic map `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Popola gli indici ElasticSearch per tutti i pacchetti:

`cradle elastic populate`

- Popola gli indici ElasticSearch per uno specifico pacchetto:

`cradle elastic populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>
