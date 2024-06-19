---
layout: page
title: common/a2ping (Nederlands)
description: "Converteer afbeeldingen in EPS- of PDF-bestanden."
content_hash: 571067aaeea8960dc5e78085b555535f8b3e549b
last_modified_at: 2024-06-19
related_topics:
  - title: বাংলা version
    url: /bn/common/a2ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/a2ping.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/a2ping.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/a2ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/a2ping.html
    icon: bi bi-globe
tldri18n_status: 2
---
# a2ping

Converteer afbeeldingen in EPS- of PDF-bestanden.
Meer informatie: <https://manned.org/a2ping>.

- Converteer een afbeelding naar PDF (Let op: het opgeven van een uitvoerbestandsnaam is optioneel):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/afbeelding.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer.pdf</span>

- Comprimeer het document met behulp van de opgegeven methode:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Scan HiResBoundingBox indien aanwezig (Let op: de standaard is yes):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sta pagina-inhoud onder en links van de oorsprong toe (Let op: de standaard is no):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef extra argumenten door aan `gs`:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef extra argumenten mee aan het externe programma (bijv. `pdftops`):

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arguments</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de help:

`a2ping -h`
