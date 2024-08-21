---
layout: page
title: windows/more (Nederlands)
description: "Toon gepagineerde uitvoer van `stdin` of een bestand."
content_hash: da7ec2cf1e1b2f0f73af4beb9b69388fc01baba2
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/windows/more.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/more.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/more.html
    icon: bi bi-globe
tldri18n_status: 2
---
# more

Toon gepagineerde uitvoer van `stdin` of een bestand.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/more>.

- Toon gepagineerde uitvoer van `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo test</span>` | more`

- Toon gepagineerde uitvoer van één of meer bestanden:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>

- Zet tabs om naar het opgegeven aantal spaties:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` /t`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">spaties</span>

- Wis het scherm voordat de pagina wordt weergegeven:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` /c`

- Toon de uitvoer beginnend bij regel 5:

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>

- Schakel uitgebreide interactieve modus in (zie help voor gebruik):

`more `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\bestand</span>` /e`

- Toon help:

`more /?`
