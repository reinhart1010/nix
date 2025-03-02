---
layout: page
title: common/test (Nederlands)
description: "Controleer bestandstypen en vergelijk waarden."
content_hash: 5634df13c03f7fb42d9a4f7a74f02251c86bc437
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/test.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/test.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/test.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/test.html
    icon: bi bi-globe
tldri18n_status: 2
---
# test

Controleer bestandstypen en vergelijk waarden.
Retourneert 0 als de voorwaarde waar is, 1 als de voorwaarde onwaar is.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/test-invocation.html>.

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
