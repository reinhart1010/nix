---
layout: page
title: common/tail (Nederlands)
description: "Toon het laatste deel van een bestand."
content_hash: 1a28a83e151f69b5eecad373830dfe23983304c4
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/common/tail.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/tail.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tail.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/tail.html
    icon: bi bi-globe
  - title: sh version
    url: /sh/common/tail.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tail.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tail

Toon het laatste deel van een bestand.
Bekijk ook: `head`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Toon laatste aantal regels in een bestand:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon een bestand vanaf een specifiek regelnummer:

`tail --lines +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon een specifiek aantal bytes vanaf het einde van een opgegeven bestand:

`tail --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de laatste regels van een bestand en blijf het bestand lezen tot `Ctrl + C`:

`tail --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Blijf het bestand lezen tot `Ctrl + C`, ook als het bestand niet toegangelijk is:

`tail --retry --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon de laatste aantal regels in een bestand en ververs iedere 'n' seconden:

`tail --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>` --sleep-interval `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>` --follow `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
