---
layout: page
title: openbsd/chpass (Nederlands)
description: "Gebruikersdatabase informatie toevoegen of wijzigen, inclusief login shell en wachtwoord."
content_hash: b0102fd958b85fee157ee298b94dca1a029cecec
last_modified_at: 2024-05-10
related_topics:
  - title: English version
    url: /en/openbsd/chpass.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/openbsd/chpass.html
    icon: bi bi-globe
tldri18n_status: 2
---
# chpass

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
