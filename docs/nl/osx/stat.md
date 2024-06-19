---
layout: page
title: osx/stat (Nederlands)
description: "Toon bestandsstatus."
content_hash: 2853c4cd789ddd3dea76bcdb706b28c4508ab32d
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/osx/stat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/stat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stat

Toon bestandsstatus.
Meer informatie: <https://keith.github.io/xcode-man-pages/stat.1.html>.

- Toon bestandseigenschappen zoals grootte, permissies, aanmaak- en toegangsdatums en meer:

`stat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Zelfde als hierboven maar uitgebreid (meer vergelijkbaar met Linux's `stat`):

`stat -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon alleen octale bestandspermissies:

`stat -f %Mp%Lp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon eigenaar en groep van het bestand:

`stat -f "%Su %Sg" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de grootte van het bestand in bytes:

`stat -f "%z %N" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
