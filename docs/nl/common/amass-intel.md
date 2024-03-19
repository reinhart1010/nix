---
layout: page
title: common/amass-intel (Nederlands)
description: "Verzamel open source informatie over een organisatie, zoals hoofddomeinen en ASN's."
content_hash: 07a6f9d32243a09b200d43c2c5936fa4c212bd38
last_modified_at: 2024-03-19
related_topics:
  - title: English version
    url: /en/common/amass-intel.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/amass-intel.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/amass-intel.html
    icon: bi bi-globe
tldri18n_status: 2
---
# amass intel

Verzamel open source informatie over een organisatie, zoals hoofddomeinen en ASN's.
Meer informatie: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Vind hoofddomeinen in een range van IP adressen:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Gebruik actieve verkenningsmethoden:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Vind hoofddomeinen gerelateerd aan een domein:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Vind ASN's die bij een [org]anisatie horen:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatienaam</span>

- Vind hoofddomeinen die bij een bepaald ASN horen:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- Sla de resultaten op in een tekstbestand:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoer_bestand</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Toon alle beschikbare databronnen:

`amass intel -list`
