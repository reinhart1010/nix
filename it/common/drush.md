---
layout: page
title: common/drush (italiano)
description: "Shell da linea di comando ed interfaccia di scripting per Drupal."
content_hash: 5d0957a3b115bf48835944367f3c8b3b99045977
related_topics:
  - title: English version
    url: /en/common/drush.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/drush.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># drush

Shell da linea di comando ed interfaccia di scripting per Drupal.
Maggiori informazioni: <https://www.drush.org>.

- Scarica il modulo "foo":

`drush dl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Scarica la versione 7.x-2.1-beta1 del modulo "foo":

`drush dl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>`-7.x-2.1-beta1`

- Abilita il modulo "foo":

`drush en `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Disabilita il modulo "foo":

`drush dis `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">foo</span>

- Pulisci tutte le cache:

`drush cc all`

- Pulisci le cache CSS e JavaScript:

`drush cc css-js`
