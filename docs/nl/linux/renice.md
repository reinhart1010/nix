---
layout: page
title: linux/renice (Nederlands)
description: "Verander de scheduleringsprioriteit/niceness van lopende processen."
content_hash: 2332ca4f7881fd1150a12102e2d52258d1fd9041
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/linux/renice.html
    icon: bi bi-globe
tldri18n_status: 2
---
# renice

Verander de scheduleringsprioriteit/niceness van lopende processen.
Niceness waarden variëren van -20 (meest gunstig voor het proces) tot 19 (minst gunstig voor het proces).
Zie ook: `nice`.
Meer informatie: <https://manned.org/renice>.

- Stel de absolute prioriteit van een lopend [p]roces in:

`renice `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+3</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Verhoog/verlaag de prioriteit van alle processen die eigendom zijn van een [g]ebruiker:

`renice --relative `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-4</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uid|user</span>

- Stel de prioriteit in van alle processen die behoren tot een proces[g]roep:

`renice --absolute `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">proces_groep</span>
