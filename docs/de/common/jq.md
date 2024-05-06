---
layout: page
title: common/jq (Deutsch)
description: "Ein JSON-Verarbeiter für die Kommandozeile mit einer domänenspezifischen Sprache."
content_hash: e8ad17dca5e9478126e9606ebcb94fe7a0c3cde9
last_modified_at: 2024-05-06
related_topics:
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/jq.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/jq.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jq

Ein JSON-Verarbeiter für die Kommandozeile mit einer domänenspezifischen Sprache.
Weitere Informationen: <https://jqlang.github.io/jq/manual/>.

- Führe den angegebenen Ausdruck aus (gib farbiges und formatiertes JSON aus):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '.'`

- Führe ein gegebenes Skript aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq --from-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/skript.jq</span>

- Übergib bestimmte Argumente:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--arg "name1" "wert1" --arg "name2" "wert2" ...</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">. + $ARGS.named</span>`'`

- Gib bestimmte Schlüssel aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.schlüssel1, .schlüssel2, ...</span>`'`

- Gib bestimmte Listenelemente aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.[index1], .[index2], ...</span>`'`

- Gib alle Listenelemente/Objektschlüssel aus:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '.[]'`

- Füge bestimmte Schlüssel hinzu/lösche bestimmte Schlüssel:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '. `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"schlüssel1": "wert1", "schlüssel2": "wert2", ...}</span>`'`
