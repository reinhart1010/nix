---
layout: page
title: common/nohup (Nederlands)
description: "Laat een proces doorgaan wanneer de terminal wordt beëindigd."
content_hash: ad84ab533c6b30c28bf580c065c361c5c55418bd
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/nohup.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/nohup.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/nohup.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/nohup.html
    icon: bi bi-globe
  - title: svenska version
    url: /sv/common/nohup.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/nohup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nohup

Laat een proces doorgaan wanneer de terminal wordt beëindigd.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html>.

- Voer een proces uit dat kan doorgaan na het sluiten van de terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>

- Start `nohup` in de achtergrondmodus:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` &`

- Voer een shell-script uit dat kan doorgaan na het sluiten van de terminal:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/script.sh</span>` &`

- Voer een proces uit en schrijf de uitvoer naar een specifiek bestand:

`nohup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argument1 argument2 ...</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/uitvoer_bestand</span>` &`
