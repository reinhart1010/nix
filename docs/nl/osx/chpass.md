---
layout: page
title: osx/chpass (Nederlands)
description: "Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord."
content_hash: e99d62dc3c17e41de03eb693fd55afcd8d9c9e02
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/osx/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
Let op: het is niet mogelijk om een gebruikerswachtwoord te wijzigen op een Open Directory systeem, gebruik hiervoor `passwd`.
Bekijk ook: `passwd`.
Meer informatie: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Voeg toe of pas interactief de gebruikersdatabase informatie aan voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Pas het gebruikersrecord aan in de directory node op de opgegeven [l]ocatie:

`chpass -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">locatie</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Gebruik de opgegeven gebr[u]ikersnaam bij het authenticeren van het mapknooppunt dat de gebruiker bevat:

`chpass -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auth_naam</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
