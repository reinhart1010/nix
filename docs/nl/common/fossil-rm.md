---
layout: page
title: common/fossil-rm (Nederlands)
description: "Verwijder bestanden of mappen uit Fossil versiebeheer."
content_hash: 69d41dd3b5161ef7c161b0b4da65b3cef72785f7
last_modified_at: 2023-11-25
related_topics:
  - title: English version
    url: /en/common/fossil-rm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-rm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil rm

Verwijder bestanden of mappen uit Fossil versiebeheer.
Zie ook: `fossil forget`.
Meer informatie: <https://fossil-scm.org/home/help/rm>.

- Verwijder een bestand of map uit Fossil versiebeheer:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Verwijder een bestand of map uit Fossil versiebeheer en verwijder het ook van de schijf:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Voeg alle vorige verwijderde en niet vastgelegde bestanden toe aan Fossil versiebeheer:

`fossil rm --reset`
