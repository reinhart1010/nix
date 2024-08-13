---
layout: page
title: linux/chfn (Nederlands)
description: "Werk de `finger`-informatie bij voor een gebruiker."
content_hash: 220b1a77f3abce66a2b9233894f398d3f047298b
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/chfn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chfn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chfn

Werk de `finger`-informatie bij voor een gebruiker.
Meer informatie: <https://manned.org/chfn>.

- Werk het "Naam"-veld van een gebruiker bij in de uitvoer van `finger`:

`chfn -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuwe_weergavenaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Werk het "Kantoornummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuw_kantoornummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Werk het "Kantoor Telefoonnummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuw_kantoor_telefoonnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Werk het "Thuis Telefoonnummer"-veld van een gebruiker bij voor de uitvoer van `finger`:

`chfn -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nieuw_thuis_telefoonnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
