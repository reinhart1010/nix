---
layout: page
title: common/pr (Nederlands)
description: "Pagineer of kolomeer bestanden voor afdrukken."
content_hash: 589682e96f1182fb864c3fbb776e48df22dde4d1
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/pr.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pr

Pagineer of kolomeer bestanden voor afdrukken.
Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- Toon meerdere bestanden met een standaardkop- en voettekst:

`pr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon met een aangepaste gecentreerde koptekst:

`pr -h "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">koptekst</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon met genummerde regels en een aangepast datumnotatieformaat:

`pr -n -D "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">formaat</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon alle bestanden samen, één in elke kolom, zonder kop- of voettekst:

`pr -m -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon, beginnend bij pagina 2 en tot en met pagina 5, met een gegeven paginalengte (inclusief kop- en voettekst):

`pr +2:5 -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paginalengte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>

- Toon met een offset voor elke regel en een afkappende aangepaste paginabreedte:

`pr -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>` -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">breedte</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand1 pad/naar/bestand2 ...</span>
