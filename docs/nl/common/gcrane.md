---
layout: page
title: common/gcrane (Nederlands)
description: "Beheer tool voor containerafbeeldingen."
content_hash: e89b1438b241a95db776838ee5717ea3b6c9192d
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/gcrane.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/gcrane.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane

Beheer tool voor containerafbeeldingen.
Deze tool implementeert een superset van de `crane`-commando's, met aanvullende commando's die specifiek zijn voor `gcr.io`.
Sommige subcommando's zoals `append`, `auth`, `copy`, enz. hebben hun eigen gebruiksdocumentatie die te vinden is onder `crane`.
Sommige subcommando's zoals `completion`, `gc`, `help` zijn specifiek voor gcrane en hebben hun eigen gebruiksdocumentatie.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Voer een `gcrane`-subcommando uit:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Sta het pushen van niet-distributieve (vreemde) lagen toe:

`gcrane --allow-nondistributable-artifacts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Sta het ophalen van afbeeldingsreferenties zonder TLS toe:

`gcrane --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Specificeer het platform in de vorm os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span>` (bijv. linux/amd64). (standaard alles):

`gcrane --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Schakel debuglogs in:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-v|--verbose</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcommand</span>

- Toon de help:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
