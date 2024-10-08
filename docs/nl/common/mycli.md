---
layout: page
title: common/mycli (Nederlands)
description: "Een command-line client voor MySQL die automatische aanvulling en syntaxisaccentuering kan uitvoeren."
content_hash: a3e8020eddb20dba546289c9ced0e918e146b1c2
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/common/mycli.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mycli

Een command-line client voor MySQL die automatische aanvulling en syntaxisaccentuering kan uitvoeren.
Meer informatie: <https://mycli.net>.

- Verbinden met een lokale database op poort 3306, met de gebruikersnaam van de huidige gebruiker:

`mycli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>

- Verbinden met een database (gebruiker wordt gevraagd om een wachtwoord):

`mycli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>

- Verbinden met een database op een andere host:

`mycli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_host</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">database_naam</span>
