---
layout: page
title: common/grep (dansk)
description: "Find mønstre i filer via regulære udtryk (regular expressions)."
content_hash: 5453e1099cd700705bceb851de0b743af0c19480
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/grep.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/grep.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/grep.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/grep.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/grep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/grep.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/grep.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/grep.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/grep.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/grep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# grep

Find mønstre i filer via regulære udtryk (regular expressions).
Mere information: <https://www.gnu.org/software/grep/manual/grep.html>.

- Søg efter et mønster i en fil:

`grep "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Søg efter en eksakt streng (deaktiverer regulære udtryk):

`grep --fixed-strings "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eksakt_streng</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Søg efter et mønster i alle filer, pånær binære, rekursivt i en mappe. Vis linjenumre der matcher til mønstret:

`grep --recursive --line-number --binary-files=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">without-match</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/mappe</span>

- Brug udvidede regulære udtryk (understøtter `?`, `+`, `{}`, `()` og `|`), i case-insensitive modus:

`grep --extended-regexp --ignore-case "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Print 3 linjer af kontekst omkring, før eller efter hvert match:

`grep --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">context|before-context|after-context</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Print, filnavn og linjenummer for hvert match, med farveoutput:

`grep --with-filename --line-number --color=always "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Søg efter linjer som matcher et mønster. Print kun den matchende tekst:

`grep --only-matching "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>

- Søg i `stdin` efter linjer der ikke matcher et mønster:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sti/til/fil</span>` | grep --invert-match "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">søgemønster</span>`"`
