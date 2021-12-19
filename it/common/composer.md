---
layout: page
title: common/composer (italiano)
description: "Un gestore di dipendenze a pacchetti per progetti PHP."
content_hash: a020ea8725eba8f279f8b7b089373d5725308a5b
related_topics:
  - title: English version
    url: /en/common/composer.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/composer.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/composer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

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
