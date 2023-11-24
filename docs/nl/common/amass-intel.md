---
layout: page
title: common/amass-intel (Nederlands)
description: "Verzamel open source informatie over een organisatie, zoals hoofddomeinen en ASN's."
content_hash: ff2bfda6106f16661efa125eb2b2a02d88c1be14
last_modified_at: 2023-11-24
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/amass-intel.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># amass intel

Verzamel open source informatie over een organisatie, zoals hoofddomeinen en ASN's.
Meer informatie: <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Vind hoofddomeinen in een range van IP adressen:

`amass intel -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Gebruik actieve verkenningsmethoden:

`amass intel -active -addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.0.1-254</span>

- Vind hoofddomeinen gerelateerd aan een domein:

`amass intel -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>

- Vind ASN's die bij een organisatie horen:

`amass intel -org `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organisatienaam</span>

- Vind hoofddomeinen die bij een bepaald ASN horen:

`amass intel -asn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asn</span>

- Sla de resultaten op in een tekstbestand:

`amass intel -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uitvoer_bestand</span>` -whois -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">domeinnaam</span>
