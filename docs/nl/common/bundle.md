---
layout: page
title: common/bundle (Nederlands)
description: "Dependency manager voor de Ruby programmeertaal."
content_hash: 8fdf0090bad3d6f4c4cd49ecd1138b3b2e2acbf1
last_modified_at: 2023-12-04
related_topics:
  - title: English version
    url: /en/common/bundle.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/bundle.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/bundle.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/bundle.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/bundle.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundle

Dependency manager voor de Ruby programmeertaal.
Meer informatie: <https://bundler.io/man/bundle.1.html>.

- Installeer alle gems gedefineerd in de `Gemfile`, welke verwacht word in de huidige map:

`bundle install`

- Voer een commando uit in de context van de huidige bundle:

`bundle exec `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumenten</span>

- Update alle gems volgens de regels gedefineerd in de `Gemfile` en regenereer de `Gemfile.lock`:

`bundle update`

- Update een of meerdere specifieke gem(s) gedefineerd in de `Gemfile`:

`bundle update `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_naam1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_naam2</span>

- Update een of meerdere specifieke gem(s) gedefineerd in de `Gemfile` maar alleen naar de volgende patch versie:

`bundle update --patch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_naam1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_naam2</span>

- Update alle gems binnen de gegeven groep in de `Gemfile`:

`bundle update --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">development</span>

- Toon de geïnstalleerde gems in de `Gemfile` welke  nieuwere versies beschikbaar hebben:

`bundle outdated`

- Maak een nieuw gem skelet:

`bundle gem `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gem_naam</span>
