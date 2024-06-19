---
layout: page
title: common/fold (Nederlands)
description: "Breek elke regel in een invoerbestand af om in een gespecificeerde breedte te passen en toon het in `stdout`."
content_hash: cd88c02e37a37c69b4e8806974415e61acdb9b1a
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/fold.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fold

Breek elke regel in een invoerbestand af om in een gespecificeerde breedte te passen en toon het in `stdout`.
Meer informatie: <https://manned.org/fold.1p>.

- Breek elke regel af op de standaard breedte (80 tekens):

`fold `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek elke regel af op een breedte van "30":

`fold -w30 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Breek elke regel af op een breedte van "5" en breek de regel bij spaties (zet elk door spaties gescheiden woord op een nieuwe regel, woorden langer dan 5 tekens worden afgebroken):

`fold -w5 -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>
