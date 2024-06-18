---
layout: page
title: osx/indent (Nederlands)
description: "Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen."
content_hash: 3b1ea2c4a94e0c0f6289887607fd16dcdbbffe04
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/osx/indent.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/indent.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/indent.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># indent

Wijzig het uiterlijk van een C/C++-programma door spaties in te voegen of te verwijderen.
Meer informatie: <https://keith.github.io/xcode-man-pages/indent.1.html>.

- Formatteer C/C++-broncode volgens de Berkeley-stijl:

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/ingesprongen_bestand.c</span>` -nbad -nbap -bc -br -c33 -cd33 -cdb -ce -ci4 -cli0 -di16 -fc1 -fcb -i4 -ip -l75 -lp -npcs -nprs -psl -sc -nsob -ts8`

- Formatteer C/C++-broncode volgens de stijl van Kernighan & Ritchie (K&R):

`indent `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bronbestand.c</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/ingesprongen_bestand.c</span>` -nbad -bap -nbc -br -c33 -cd33 -ncdb -ce -ci4 -cli0 -cs -d0 -di1 -nfc1 -nfcb -i4 -nip -l75 -lp -npcs -nprs -npsl -nsc -nsob`
