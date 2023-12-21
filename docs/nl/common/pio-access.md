---
layout: page
title: common/pio-access (Nederlands)
description: "Stel het toegangsniveau in op publieke bronnen (pakketten) in het register."
content_hash: 5314384fdd416461d4d4302c94561fafb98f7238
last_modified_at: 2023-12-21
related_topics:
  - title: English version
    url: /en/common/pio-access.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pio access

Stel het toegangsniveau in op publieke bronnen (pakketten) in het register.
Meer informatie: <https://docs.platformio.org/en/latest/core/userguide/access/>.

- Verleen een gebruiker toegang tot een bron:

`pio access grant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">guest|maintainer|admin</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_urn</span>

- Verwijder de toegang voor een gebruiker tot een bron:

`pio access revoke `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_urn</span>

- Toon alle bronnen waartoe een gebruiker of team toegang tot heeft en het toegangsniveau:

`pio access list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Beperk de toegang tot een bron voor specifieke gebruikers of teamleden:

`pio access private `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_urn</span>

- Verleen alle gebruikers toegang tot een bron:

`pio access public `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_urn</span>
