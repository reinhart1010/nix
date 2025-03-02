---
layout: page
title: common/dircolors (Nederlands)
description: "Geef commando's weer om de LS_COLOR-omgevingsvariabele in te stellen en style `ls`, `dir` enz."
content_hash: d12668b22e7cd8c83234a20b3e03ed8874102f74
last_modified_at: 2024-12-22
related_topics:
  - title: English version
    url: /en/common/dircolors.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dircolors.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dircolors.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dircolors

Geef commando's weer om de LS_COLOR-omgevingsvariabele in te stellen en style `ls`, `dir` enz.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/dircolors-invocation.html>.

- Geef commando's weer om LS_COLOR in te stellen met standaardkleuren:

`dircolors`

- Toon ieder bestandstype met de kleur zoals deze in `ls` getoond zou worden:

`dircolors --print-ls-colors`

- Geef commando's weer om LS_COLOR in te stellen met kleuren uit een bestand:

`dircolors `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Geef commando's weer voor de Bourne-shell:

`dircolors --bourne-shell`

- Geef commando's weer voor de C-shell:

`dircolors --c-shell`

- Bekijk de standaardkleuren voor bestandstypen en extensies:

`dircolors --print-data`
