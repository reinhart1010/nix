---
layout: page
title: freebsd/chpass (Nederlands)
description: "Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord."
content_hash: efe073f75daa0e4b76d8377044897e2654a835cf
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/freebsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/freebsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
Bekijk ook: `passwd`.
Meer informatie: <https://man.freebsd.org/cgi/man.cgi?chpass>.

- Voeg toe of pas interactief de gebruikersdatabase informatie aan voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Pas de account v[e]rloop tijd aan (in seconden vanaf de epoch, UTC):

`su -c 'chpass -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tijd</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`'`

- Pas een gebruikerswachtwoord aan::

`su -c 'chpass -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gecodeerd_wachtwoord</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`'`

- Specificeer een [h]ostnaam of adres van een NIS server:

`su -c 'chpass -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`'`

- Specificeer een specifiek [d]omein (standaard systeem domein naam):

`su -c 'chpass -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>`'`
