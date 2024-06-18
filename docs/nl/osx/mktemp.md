---
layout: page
title: osx/mktemp (Nederlands)
description: "Maak een tijdelijk bestand of een tijdelijke map aan."
content_hash: e2e6230c6f54161d50a15e7f20321c908dec177a
last_modified_at: 2024-06-18
related_topics:
  - title: English version
    url: /en/osx/mktemp.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/mktemp.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/osx/mktemp.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mktemp

Maak een tijdelijk bestand of een tijdelijke map aan.
Meer informatie: <https://keith.github.io/xcode-man-pages/mktemp.1.html>.

- Maak een leeg tijdelijk bestand en toon het absolute pad:

`mktemp`

- Gebruik een aangepaste map (standaard is de uitvoer van `getconf DARWIN_USER_TEMP_DIR`, of `/tmp`):

`mktemp --tmpdir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/pad/naar/tempdir</span>

- Gebruik een aangepast pad-sjabloon (`X`en worden vervangen door willekeurige alfanumerieke tekens):

`mktemp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/tmp/voorbeeld.XXXXXXXX</span>

- Gebruik een aangepaste bestandsnaam-prefix:

`mktemp -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorbeeld</span>

- Maak een lege tijdelijke map aan en toon het absolute pad:

`mktemp --directory`
