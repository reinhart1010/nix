---
layout: page
title: common/cmp (Nederlands)
description: "Vergelijk twee bestanden byte voor byte."
content_hash: b31d325203a771387fb9fc1bb21fa53c1ee1396b
last_modified_at: 2023-11-13
related_topics:
  - title: English version
    url: /en/common/cmp.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/cmp.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cmp.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cmp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cmp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cmp

Vergelijk twee bestanden byte voor byte.
Meer informatie: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Toon karakter en regelnummer van het eerste verschil tussen twee bestanden:

`cmp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Toon info van het eerste verschil: karakter, regelnummer, bytes en waardes:

`cmp --print-bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Toon de byte nummers en waardes van ieder verschil:

`cmp --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>

- Vergelijk bestanden, maar toon niets, pak alleen de exit status:

`cmp --quiet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand2</span>
