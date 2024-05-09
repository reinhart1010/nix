---
layout: page
title: netbsd/chpass (Nederlands)
description: "Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord."
content_hash: 9b3c966d94158a55934df84eeba860abc31795d6
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/netbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/netbsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
Bekijk ook: `passwd`.
Meer informatie: <https://man.openbsd.org/chsh>.

- Stel interactief een specifieke login shell in voor de huidige gebruiker:

`su -c chpass`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`chpass -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login [s]hell in voor een specifieke gebruiker:

`chpass chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Specificeer een gebruikersdatabase entry in het `passwd` bestandsformaat:

`su -c 'chpass -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam:gecodeerd_wachtwoord:uid:gid:...</span>` -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Pas alleen het lokale wachtwoord bestand aan:

`su -c 'chpass -l -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Pas geforceerd een database [y]P wachtwoord database entry aan:

`su -c 'chpass -y -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>
