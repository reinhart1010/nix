---
layout: page
title: common/expand (Nederlands)
description: "Vervang tabs met spaties."
content_hash: d9457aaff1b08a4dd60e7295842470780177d121
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/expand.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/expand.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/expand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expand

Vervang tabs met spaties.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- Vervang tabs in ieder bestand met spaties en schrijf het naar `stdout`:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Vervang tabs met spaties, lezend vanaf `stdin`:

`expand`

- Vervang geen tabs na een karakter:

`expand -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Laat tabs een bepaald aantal tekens uit elkaar staan, niet 8:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Gebruik een door komma's gescheiden lijst met expliciete tabposities:

`expand -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1,4,6</span>
