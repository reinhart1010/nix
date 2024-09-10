---
layout: page
title: common/touch (Nederlands)
description: "Maak bestanden aan en stel toegang-/wijzigingstijden in."
content_hash: 8b6c6155402e3a23d13dc67c3d641fff6874169b
last_modified_at: 2024-09-10
related_topics:
  - title: català version
    url: /ca/common/touch.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/touch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/touch.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/touch.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/touch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/touch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/touch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/touch.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/touch.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/touch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# touch

Maak bestanden aan en stel toegang-/wijzigingstijden in.
Meer informatie: <https://manned.org/touch>.

- Maak specifieke bestanden aan:

`touch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Stel de toeg[a]ng- of wijzigingstijden ([m]) van een bestand in op de huidige tijd en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a|m</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Stel de [t]ijd van een bestand in op een specifieke waarde en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">YYYYMMDDHHMM.SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Stel de timestamp van de bestanden in op die van het [r]eferentiebestand en maak ([c]) geen bestand aan als deze niet bestaat:

`touch -c -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/referentiebestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
