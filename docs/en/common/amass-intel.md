---
layout: page
title: common/amass-intel (English)
description: "Collect open source intel on an organisation like root domains and ASNs."
content_hash: 88d59b5ebd778ba48b1d5fb384f364297ee3c4ea
last_modified_at: 2024-03-17
related_topics:
  - title: español version
    url: /es/common/amass-intel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-intel.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/amass-intel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass intel

Collect open source intel on an organisation like root domains and ASNs.
More information: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Find root domains in an IP [addr]ess range:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Use active recon methods:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Find root domains related to a [d]omain:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Find ASNs belonging to an [org]anisation:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisation_name</span>

- Find root domains belonging to a given Autonomous System Number:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- Save results to a text file:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- List all available data sources:

`amass intel -list`
