---
layout: page
title: common/crane (Nederlands)
description: "Hulpmiddel voor het beheren van containerimages."
content_hash: d3983baf5fad06cb1dde65904af667e9b84f49a4
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/crane.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane

Hulpmiddel voor het beheren van containerimages.
Sommige subcommando's zoals `pull`, `push`, `copy`, enz. hebben hun eigen gebruiksdocumentatie.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md/>.

- Voer een `crane` subcommando uit:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Sta het pushen van niet-distribueerbare (buitenlandse) lagen toe:

`crane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Sta het ophalen van afbeeldingsreferenties zonder TLS toe:

`crane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Geef het platform op in de vorm os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` (bijv. linux/amd64). (standaard alle):

`crane --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Schakel debuglogs in voor een subcommando:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Toon help voor een subcommando:

`crane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>
