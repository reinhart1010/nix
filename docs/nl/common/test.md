---
layout: page
title: common/test (Nederlands)
description: "Controleer bestandstypen en vergelijk waarden."
content_hash: b03e8edc0e157a90ef9b733f32e7f415bdfe11b0
last_modified_at: 2024-06-28
related_topics:
  - title: English version
    url: /en/common/test.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/test.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/test.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/test.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># test

Controleer bestandstypen en vergelijk waarden.
Retourneert 0 als de voorwaarde waar is, 1 als de voorwaarde onwaar is.
Meer informatie: <https://www.gnu.org/software/coreutils/test>.

- Test of een gegeven variabele gelijk is aan een gegeven string:

`test "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$MY_VAR</span>`" = "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/bin/zsh</span>`"`

- Test of een gegeven variabele leeg is:

`test -z "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GIT_BRANCH</span>`"`

- Test of een bestand bestaat:

`test -f "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand_of_map</span>`"`

- Test of een map niet bestaat:

`test ! -d "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/map</span>`"`

- Als A waar is, voer dan B uit, of C in het geval van een fout (let op dat C mogelijk wordt uitgevoerd, zelfs als A mislukt):

`test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">voorwaarde</span>` && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "true"</span>` || `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">echo "false"</span>
