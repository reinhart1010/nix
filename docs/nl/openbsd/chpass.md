---
layout: page
title: openbsd/chpass (Nederlands)
description: "Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord."
content_hash: b0102fd958b85fee157ee298b94dca1a029cecec
last_modified_at: 2024-05-09
related_topics:
  - title: English version
    url: /en/openbsd/chpass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/openbsd/chpass.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chpass

Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord.
Bekijk ook: `passwd`.
Meer informatie: <https://man.openbsd.org/chsh>.

- Stel interactief een specifieke login shell in voor de huidige gebruiker:

`doas chsh`

- Stel een specifieke login [s]hell in voor de huidige gebruiker:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>

- Stel een login [s]hell in voor een specifieke gebruiker:

`doas chsh -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/shell</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Specificeer een gebruikersdatabase entry in het `passwd` bestandsformaat:

`doas chsh -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam:gecodeerd_wachtwoord:uid:gid:...</span>
