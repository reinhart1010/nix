---
layout: page
title: common/readarray (Nederlands)
description: "Lees regels van `stdin` in een array."
content_hash: 1a7961990671b433576316ac56c627fbe6b7ec67
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/common/readarray.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/readarray.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># readarray

Lees regels van `stdin` in een array.
Meer informatie: <https://www.gnu.org/software/bash/manual/bash.html#index-readarray>.

- Interactief regels in een array invoeren:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_naam</span>

- Lees regels uit een bestand en plaats ze in een array:

`readarray `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_naam</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.txt</span>

- Verwijder scheidingstekens aan het einde (standaard newline):

`readarray -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_naam</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.txt</span>

- Kopieer maximaal het opgegeven aantal regels:

`readarray -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">array_naam</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand.txt</span>
