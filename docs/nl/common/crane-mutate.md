---
layout: page
title: common/crane-mutate (Nederlands)
description: "Wijzig image-labels en annotaties."
content_hash: 8f9cea34c593142d620d2bcf4c0db7985f2890f9
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/crane-mutate.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-mutate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane mutate

Wijzig image-labels en annotaties.
De container moet naar een registry worden gepusht, en het manifest wordt daar bijgewerkt.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_mutate.md>.

- Nieuwe annotaties om in te stellen (standaard []):

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--annotation</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-l|--label</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">annotation/label</span>

- Pad naar tarball/opdracht/entrypoint/omgeving variabele/exposed-ports om aan de image toe te voegen:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--append</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--cmd</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--entrypoint</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-e|--env</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--exposed-ports</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">var1 var2 ...</span>

- Pad naar nieuwe tarball van de resulterende image:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-o|--output</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/tarball</span>

- Repository in de vorm os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,<platform></span>` om de gewijzigde image te pushen:

`crane mutate --set-platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform_naam</span>

- Nieuwe tagreferentie die moet worden toegepast op de gewijzigde image:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Nieuwe gebruiker in te stellen:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-u|--user</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Nieuwe werk-map in te stellen:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-w|--workdir</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/werk-map</span>

- Toon de help:

`crane mutate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
