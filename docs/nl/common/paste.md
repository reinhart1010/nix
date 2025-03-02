---
layout: page
title: common/paste (Nederlands)
description: "Voeg regels van bestanden samen."
content_hash: 7e30d5e02d6dd5b6f1ef8cb7babf4d5052f7e2a8
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/paste.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/paste.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paste

Voeg regels van bestanden samen.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- Voeg alle regels samen tot één enkele regel, met TAB als scheidingsteken:

`paste -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voeg alle regels samen tot één enkele regel, met het opgegeven scheidingsteken:

`paste -s -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheidingsteken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met TAB als scheidingsteken:

`paste `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met het opgegeven scheidingsteken:

`paste -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">scheidingsteken</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Voeg twee bestanden samen, met afwisselend toegevoegde regels:

`paste -d '\n' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>
