---
layout: page
title: common/amass-intel (English)
description: "Collect open source intel on an organisation like root domains and ASNs."
content_hash: 37ecc38050fcf6286d9d2fae44d3c920bb2f7d80
---
# amass intel

Collect open source intel on an organisation like root domains and ASNs.
More information: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Find root domains in an IP address range:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Use active recon methods:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Find root domains related to a domain:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>

- Find ASNs belonging to an organisation:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisation_name</span>

- Find root domains belonging to a given Autonomous System Number:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- Save results to a text file:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">output_file</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domain_name</span>
