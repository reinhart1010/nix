---
layout: page
title: common/sort (Nederlands)
description: "Sorteer regels van tekstbestanden."
content_hash: 7c8a25e52eff8c0c597b38f8f001d2a83b864ac7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/sort.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sort.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/sort.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sort

Sorteer regels van tekstbestanden.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html>.

- Sorteer een bestand in oplopende volgorde:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sorteer een bestand in aflopende volgorde:

`sort --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sorteer een bestand op een niet-hoofdlettergevoelige manier:

`sort --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sorteer een bestand met numerieke in plaats van alfabetische volgorde:

`sort --numeric-sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sorteer `/etc/passwd` numeriek op het 3e veld van elke regel, gebruik makend van ":" als veldscheidingsteken:

`sort --field-separator=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- Sorteer zoals hierboven, maar wanneer items in het 3e veld gelijk zijn, sorteer op het 4e veld met getallen en exponenten:

`sort -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,3n</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4,4g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- Sorteer een bestand waarbij alleen unieke regels worden behouden:

`sort --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Sorteer een bestand en schrijf de uitvoer naar het opgegeven uitvoerbestand (kan worden gebruikt om een bestand in-place te sorteren):

`sort --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
