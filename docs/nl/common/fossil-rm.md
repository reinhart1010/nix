---
layout: page
title: common/fossil-rm (Nederlands)
description: "Verwijder bestanden of mappen uit Fossil versiebeheer."
content_hash: 83e43e59e007509605f43c48803ccfe93872c9ee
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/fossil-rm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fossil rm

Verwijder bestanden of mappen uit Fossil versiebeheer.
Bekijk ook: `fossil forget`.
Meer informatie: <https://fossil-scm.org/home/help/rm>.

- Verwijder een bestand of map uit Fossil versiebeheer:

`fossil rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Verwijder een bestand of map uit Fossil versiebeheer en verwijder het ook van de schijf:

`fossil rm --hard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>

- Voeg alle vorige verwijderde en niet vastgelegde bestanden toe aan Fossil versiebeheer:

`fossil rm --reset`
