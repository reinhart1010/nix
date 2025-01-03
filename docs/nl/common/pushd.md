---
layout: page
title: common/pushd (Nederlands)
description: "Plaats een map op een stack zodat deze later kan worden benaderd."
content_hash: 3459546c4c51ee8fe3e7bf96bafc53c12efe17ce
last_modified_at: 2025-01-03
related_topics:
  - title: dansk version
    url: /da/common/pushd.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/pushd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pushd.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/pushd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pushd

Plaats een map op een stack zodat deze later kan worden benaderd.
Bekijk ook `popd` om terug te schakelen naar de originele map en `dirs` om de inhoud van de mapstapel weer te geven.
Meer informatie: <https://www.gnu.org/software/bash/manual/html_node/Directory-Stack-Builtins.html>.

- Schakel naar een map en zet deze op de stapel:

`pushd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>

- Wissel de eerste en tweede mappen op de stapel:

`pushd`

- Draai de stapel door het 5e element bovenaan te plaatsen:

`pushd +4`

- Draai de stapel 4 keer naar links (de huidige map blijft bovenaan door het 5e element te vervangen):

`pushd -n +4`
