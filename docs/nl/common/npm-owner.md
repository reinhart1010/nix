---
layout: page
title: common/npm-owner (Nederlands)
description: "Beheer eigendom van gepubliceerde pakketten."
content_hash: 7e524f5a97826e811455e1e6a9c4cc07d04083f9
last_modified_at: 2024-11-16
related_topics:
  - title: English version
    url: /en/common/npm-owner.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/npm-owner.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/npm-owner.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># npm owner

Beheer eigendom van gepubliceerde pakketten.
Meer informatie: <https://docs.npmjs.com/cli/commands/npm-owner>.

- Voeg een nieuwe gebruiker toe als maintainer van een pakket:

`npm owner add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>

- Verwijder een gebruiker van de eigenaars-lijst van een pakket:

`npm owner rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>

- Toon alle eigenaars van een pakket:

`npm owner ls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket_naam</span>
