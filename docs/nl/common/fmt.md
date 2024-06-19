---
layout: page
title: common/fmt (Nederlands)
description: "Herformatteer een tekstbestand door de alinea's samen te voegen en de regelbreedte te beperken tot een aantal tekens (standaard 75)."
content_hash: 8310bb084058a6f9c2896fa60e3b3a1c3b4dddd9
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/fmt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/fmt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fmt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fmt

Herformatteer een tekstbestand door de alinea's samen te voegen en de regelbreedte te beperken tot een aantal tekens (standaard 75).
Meer informatie: <https://www.gnu.org/software/coreutils/fmt>.

- Herformatteer een bestand:

`fmt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Herformatteer een bestand met uitvoerregels van (hoogstens) `n` tekens:

`fmt -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Herformatteer een bestand zonder regels die korter zijn dan de opgegeven breedte samen te voegen:

`fmt -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Herformatteer een bestand met uniforme spatiëring (1 spatie tussen woorden en 2 spaties tussen alinea's):

`fmt -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
