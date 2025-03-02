---
layout: page
title: common/seq (Nederlands)
description: "Toon een reeks getallen naar `stdout`."
content_hash: a8dae383c43e64f9caba36daa0234d7cd481e3a7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/seq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/seq.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/seq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# seq

Toon een reeks getallen naar `stdout`.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html>.

- Reeks van 1 tot 10:

`seq 10`

- Elk 3e nummer van 5 tot 20:

`seq 5 3 20`

- Scheid de uitvoer met een spatie in plaats van een nieuwe regel:

`seq -s " " 5 3 20`

- Formatteer de uitvoerbreedte naar minimaal 4 cijfers, opgevuld met nullen indien nodig:

`seq -f "%04g" 5 3 20`
