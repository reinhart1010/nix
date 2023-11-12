---
layout: page
title: common/sed (dansk)
description: "Rediger tekst, programmatisk."
content_hash: 902c5f2b787f23435c250a10517d01e138e47b6a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/sed.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/sed.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/sed.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># sed

Rediger tekst, programmatisk.
Mere information: <https://www.gnu.org/software/sed/manual/sed.html>.

- Erstat den første forekomst af et regulært udtryk (regular expression) i hver linje af en fil, og print resultatet:

`sed 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Erstat alle forekomster af et regulært udtryk in en fil, og print resultatet:

`sed -r 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regular_expression</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Erstat alle forekomster af en streng i en fil, og overskriv filen:

`sed -i 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/g' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Erstat forekomster på linjer der matcher mønstret:

`sed '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linje_mønster</span>`/s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Fjern linjer der matcher mønstret:

`sed '/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">linje_mønster</span>`/d' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Print de første 11 linjer af en fil:

`sed 11q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Udfør flere find-og-erstat udtryk i en fil:

`sed -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/' -e 's/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`/' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>

- Erstat separator `/` med en hvilken som helst anden karakter ikke brugt i find- eller erstat-mønstrene, f.eks. `#`:

`sed 's#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find</span>`#`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">erstat</span>`#' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filnavn</span>
