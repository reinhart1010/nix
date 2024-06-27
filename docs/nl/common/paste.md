---
layout: page
title: common/paste (Nederlands)
description: "Voeg regels van bestanden samen."
content_hash: 701a63bdb5cfb19193b8af46234552ed2ba4473d
last_modified_at: 2024-06-27
related_topics:
  - title: English version
    url: /en/common/paste.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paste

Voeg regels van bestanden samen.
Meer informatie: <https://www.gnu.org/software/coreutils/paste>.

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
