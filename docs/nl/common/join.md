---
layout: page
title: common/join (Nederlands)
description: "Voeg regels van twee gesorteerde bestanden samen op een gemeenschappelijk veld."
content_hash: 84fe24a71e4378e616737b10958f82356868f8cf
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/join.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/join.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/join.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/join.html
    icon: bi bi-globe
tldri18n_status: 2
---
# join

Voeg regels van twee gesorteerde bestanden samen op een gemeenschappelijk veld.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- Voeg twee bestanden samen op het eerste (standaard) veld:

`join `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Voeg twee bestanden samen met een komma (in plaats van een spatie) als veldscheidingsteken:

`join -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">','</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Voeg veld 3 van bestand 1 samen met veld 1 van bestand 2:

`join -1 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` -2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Produceer een regel voor elke niet-koppelbare regel van bestand 1:

`join -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Voeg een bestand samen vanaf `stdin`:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` | join - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>
