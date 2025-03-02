---
layout: page
title: common/stty (Nederlands)
description: "Stel opties in voor een terminalapparaatinterface."
content_hash: 23e6204f2a916087ee614ca474e32dbd29efd20c
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/stty.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/stty.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/stty.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/stty.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/stty.html
    icon: bi bi-globe
tldri18n_status: 2
---
# stty

Stel opties in voor een terminalapparaatinterface.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Toon alle instellingen voor de huidige terminal:

`stty --all`

- Stel het aantal rijen of kolommen in:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rows|cols</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aantal</span>

- Verkrijg de daadwerkelijke overdrachtssnelheid van een apparaat:

`stty --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/apparaat_bestand</span>` speed`

- Reset alle modi naar redelijke waarden voor de huidige terminal:

`stty sane`

- Wissel tussen rauwe en normale modus:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">raw|cooked</span>

- Zet karakter echoing uit of aan:

`stty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-echo|echo</span>
