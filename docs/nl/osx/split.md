---
layout: page
title: osx/split (Nederlands)
description: "Split een bestand in stukken."
content_hash: 90612d7c9f989e0143ff29ada9806d45876cdba0
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/osx/split.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/split.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/split.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/split.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># split

Split een bestand in stukken.
Meer informatie: <https://keith.github.io/xcode-man-pages/split.1.html>.

- Split een bestand, elk deel heeft 10 regels (behalve het laatste deel):

`split -l 10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Split een bestand op een reguliere expressie. De overeenkomende regel zal de eerste regel van het volgende uitvoerbestand zijn:

`split -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat|^[dh]og</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Split een bestand met 512 bytes in elk deel (behalve het laatste deel; gebruik 512k voor kilobytes en 512m voor megabytes):

`split -b 512 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Split een bestand in 5 bestanden. Het bestand wordt zo gesplitst dat elk deel dezelfde grootte heeft (behalve het laatste deel):

`split -n 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
