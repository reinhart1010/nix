---
layout: page
title: common/jq (Deutsch)
description: "Ein JSON-Verarbeiter für die Kommandozeile mit einer domänenspezifischen Sprache."
content_hash: c07e14c44e87a5f47cadef5773c210e1f899a7df
related_topics:
  - title: English version
    url: /en/common/jq.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/jq.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># jq

Ein JSON-Verarbeiter für die Kommandozeile mit einer domänenspezifischen Sprache.
Weitere Informationen: <https://stedolan.github.io/jq/manual/>.

- Führe den angegebenen Ausdruck aus (gib farbiges und formatiertes JSON aus):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>`'`

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

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cat pfad/zu/datei.json</span>` | jq '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">{"schlüssel1": "wert1", "schlüssel2": "wert2", ...}</span>`'`
