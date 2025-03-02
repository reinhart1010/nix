---
layout: page
title: common/dirname (Nederlands)
description: "Berekent de bovenliggende map van een bestand of map."
content_hash: e976d30d50a4fdcb5c661a056bc1fe1dad7c9699
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/dirname.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dirname.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dirname.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/dirname.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dirname

Berekent de bovenliggende map van een bestand of map.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Bereken de bovenliggende map van een opgegeven pad:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Bereken de bovenliggende map van meerdere paden:

`dirname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>

- Scheid de uitvoer met een NUL-teken in plaats van een nieuwe regel (handig bij gebruik met `xargs`):

`dirname --zero `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...</span>
