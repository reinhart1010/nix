---
layout: page
title: linux/runcon (Nederlands)
description: "Voer een programma uit in een andere SELinux-beveiligingscontext."
content_hash: 6f7b550bc0c61c38b95daa038a41bc1964c1f843
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/runcon.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/runcon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# runcon

Voer een programma uit in een andere SELinux-beveiligingscontext.
Bekijk ook: `secon`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- Toon de beveiligingscontext van de huidige uitvoeringscontext:

`runcon`

- Specificeer het domein om een commando in uit te voeren:

`runcon -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Specificeer de context rol om een commando mee uit te voeren:

`runcon -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>`_r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Specificeer de volledige context om een commando mee uit te voeren:

`runcon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruiker</span>`_u:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rol</span>`_r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domein</span>`_t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>
