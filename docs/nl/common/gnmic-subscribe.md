---
layout: page
title: common/gnmic-subscribe (Nederlands)
description: "Abonneer op gnmic netwerk apparaat status updates."
content_hash: f413eeb6e9d3511d03c4b10eb53efcb08f47b866
last_modified_at: 2023-12-15
related_topics:
  - title: English version
    url: /en/common/gnmic-subscribe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnmic subscribe

Abonneer op gnmic netwerk apparaat status updates.
Meer informatie: <https://gnmic.kmrd.dev/cmd/subscribe>.

- Abonneer op doel status updates onder de subtree van een specifiek pad:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:poort</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>

- Abonneer op een doel met een interval van 30 seconden (standaard is 10 seconden):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:poort</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>` --sample-interval 30s`

- Abonneer op een doel met een interval en alleen op updates bij verandering:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:poort</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>` --stream-mode on-change --heartbeat-interval 1m`

- Abonneer op een doel voor alleen een update:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:poort</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>` --mode once`

- Abonneer op een doel en specificeer de response codering (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip:poort</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad</span>` --encoding json_ietf`
