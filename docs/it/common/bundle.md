---
layout: page
title: common/bundle (italiano)
description: "Gestore di dipendenze per il linguaggio di programmazione Ruby."
content_hash: 8c0135ea9a6b66383ec62005c51409978efe5137
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># bundle

Gestore di dipendenze per il linguaggio di programmazione Ruby.
Maggiori informazioni: <https://bundler.io/man/bundle.1.html>.

- Installa tutte le gem definite nel gemfile della directory corrente:

`bundle install`

- Aggiorna tutte le gem secondo le regole definite nel gemfile e genera un `gemfile.lock`:

`bundle update`

- Aggiorna una specifica gem definita nel gemfile:

`bundle update --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_gem</span>

- Crea un scheletro per una nuova gem:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_gem</span>
