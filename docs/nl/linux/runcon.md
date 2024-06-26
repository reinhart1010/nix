---
layout: page
title: linux/runcon (Nederlands)
description: "Voer een programma uit in een andere SELinux-beveiligingscontext."
content_hash: bd7b3baf744934ca8968c845ade018370a3898f5
last_modified_at: 2024-06-26
related_topics:
  - title: English version
    url: /en/linux/runcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runcon

Voer een programma uit in een andere SELinux-beveiligingscontext.
Bekijk ook: `secon`.
Meer informatie: <https://www.gnu.org/software/coreutils/runcon>.

- Toon de beveiligingscontext van de huidige uitvoeringscontext:

`runcon`

- Specificeer het domein om een commando in uit te voeren:

`runcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Specificeer de context rol om een commando mee uit te voeren:

`runcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>`_r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Specificeer de volledige context om een commando mee uit te voeren:

`runcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>`_u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>`_r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
