---
layout: page
title: common/pamfile (Nederlands)
description: "Beschrijf Netpbm (PAM or PNM) bestanden."
content_hash: 839dd79e260db133484da658ed466187c6e2b0c7
last_modified_at: 2024-06-03
related_topics:
  - title: English version
    url: /en/common/pamfile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/pamfile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pamfile

Beschrijf Netpbm (PAM or PNM) bestanden.
Meer informatie: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Beschrijf de gespecificeerde Netpbm bestanden:

`pamfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Beschrijf iedere afbeelding in ieder invoerbestand (in tegenstelling tot alleen de eerste afbeelding in elk bestand) in een machine-leesbaar formaat:

`pamfile -allimages -machine `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Toon hoeveel afbeeldingen de invoerbestanden bevatten:

`pamfile -count `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
