---
layout: page
title: common/mktemp (Nederlands)
description: "Maak een tijdelijk bestand of een tijdelijke map aan."
content_hash: 92a0cccec9cc0346dc57f9159add2118b00b111c
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/common/mktemp.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/mktemp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mktemp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mktemp

Maak een tijdelijk bestand of een tijdelijke map aan.
Meer informatie: <https://man.openbsd.org/mktemp.1>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map als `$TMPDIR` niet is ingesteld (de standaard is platformafhankelijk, maar meestal `/tmp`):

`mktemp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/tempdir</span>

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/voorbeeld.XXXXXXXX</span>

- Gebruik een aangepast bestandsnaam-sjabloon:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld.XXXXXXXX</span>

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp -d`
