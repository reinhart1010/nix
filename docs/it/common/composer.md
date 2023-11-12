---
layout: page
title: common/composer (italiano)
description: "Un gestore di dipendenze a pacchetti per progetti PHP."
content_hash: a020ea8725eba8f279f8b7b089373d5725308a5b
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/composer.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># composer

Un gestore di dipendenze a pacchetti per progetti PHP.
Maggiori informazioni: <https://getcomposer.org/>.

- Aggiungi un pacchetto come dipendenza per questo progetto, aggiungendolo a `composer.json`:

`composer require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nome_pacchetto</span>

- Installa tutte le dipendenze listate nel `composer.json` di questo progetto:

`composer install`

- Disinstalla un pacchetto da questo progetto, rimuovendolo come dipendenza da `composer.json`:

`composer remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user/nome_pacchetto</span>

- Aaggiorna tutte le dipendenze nel `composer.json` di questo progetto:

`composer update`

- Aggiorna composer alla versione più recente:

`composer self-update`
