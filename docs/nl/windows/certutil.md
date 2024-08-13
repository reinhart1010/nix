---
layout: page
title: windows/certutil (Nederlands)
description: "Een tool om certificaatinformatie te beheren en configureren."
content_hash: 13d0f945e7a17f0fcdd3c513d854c1e9f818cf90
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/windows/certutil.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/windows/certutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# certutil

Een tool om certificaatinformatie te beheren en configureren.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/certutil>.

- Dump de configuratie-informatie of bestanden:

`certutil `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Encodeer een bestand in hexadecimaal:

`certutil -encodehex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\invoer_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\uitvoer_bestand</span>

- Encodeer een bestand naar Base64:

`certutil -encode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\invoer_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\uitvoer_bestand</span>

- Decodeer een Base64-gecodeerd bestand:

`certutil -decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\invoer_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\uitvoer_bestand</span>

- Genereer en toon een cryptografische hash over een bestand:

`certutil -hashfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad\naar\invoer_bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md2|md4|md5|sha1|sha256|sha384|sha512</span>
