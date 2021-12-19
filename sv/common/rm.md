---
layout: page
title: common/rm (svenska)
description: "Ta bort filer eller mappar."
content_hash: 5cdd0564f35a84dc687aebb9646d15b0c61bcc56
related_topics:
  - title: English version
    url: /en/common/rm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/rm.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/rm.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/rm.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/rm.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/rm.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/common/rm.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/rm.html
    icon: bi bi-globe
---
# rm

Ta bort filer eller mappar.
Mer information: <https://www.gnu.org/software/coreutils/rm>.

- Ta bort filer från godtyckliga ställen:

`rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sökväg/till/fil</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sökväg/till/en/annan/fil</span>

- Rekursivt ta bort en mapp och dess undermappar:

`rm -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sökväg/till/mapp</span>

- Tvinga borttagning av en mapp utan att bekräfta eller visa felmeddelanden:

`rm -rf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sökväg/till/mapp</span>

- Interaktivt ta bort flera filer, genom att fråga om borttagning för varje fil:

`rm -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fil(er)</span>

- Ta bort filer och visa ett meddelande för varje borttagning:

`rm -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sökväg/till/mapp/*</span>
