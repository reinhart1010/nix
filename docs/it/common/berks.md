---
layout: page
title: common/berks (italiano)
description: "Gestore di dipendenze per Chef cookbooks."
content_hash: aa7384e25e42d832127c72ac4afcba555580eec8
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/berks.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/berks.html
    icon: bi bi-globe
tldri18n_status: 2
---
# berks

Gestore di dipendenze per Chef cookbooks.
Maggiori informazioni: <https://docs.chef.io/berkshelf.html>.

- Installa dipendenze cookbook in una repo locale:

`berks install`

- Aggiorna uno specifico cookbook e le sue dipendenze:

`berks update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>

- Carica un cookbook sul server di Chef:

`berks upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>

- Mostra le dipendenze di un cookbook:

`berks contingent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cookbook</span>
