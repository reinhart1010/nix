---
layout: page
title: windows/expand (Nederlands)
description: "Pak Windows Cabinet bestanden uit."
content_hash: 4094b2669c33d6008df529e9f03ce5a86752413e
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/windows/expand.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/expand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expand

Pak Windows Cabinet bestanden uit.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- Pak een Cabinet bestand met één bestand naar de specifieke map:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>

- Toon een lijst van bestanden in een Cabinet bestand:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>` -d`

- Pak alle bestanden van een Cabinet bestand uit:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>` -f:*`

- Pak een specifiek bestand van een Cabinet bestand uit:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>` -f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Negeer de mapstructuur bij het uitpakken en voeg ze toe aan een enkele map:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\map</span>` -i`
