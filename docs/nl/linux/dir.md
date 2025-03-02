---
layout: page
title: linux/dir (Nederlands)
description: "Toon de inhoud van een directory met één regel per bestand, speciale tekens worden weergegeven met backslash-escape-sequenties."
content_hash: 05c579a2dc6e32edb4291f5e2d82de391703ac00
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/dir.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dir.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dir

Toon de inhoud van een directory met één regel per bestand, speciale tekens worden weergegeven met backslash-escape-sequenties.
Werkt als `ls -C --escape`.
Meer informatie: <https://manned.org/dir>.

- Toon alle bestanden, inclusief verborgen bestanden:

`dir --all`

- Toon bestanden inclusief hun auteur (`-l` is vereist):

`dir -l --author`

- Toon bestanden en sluit degenen uit die overeenkomen met een specifiek patroon:

`dir --hide=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">patroon</span>

- Toon subdirectories recursief:

`dir --recursive`

- Toon de help:

`dir --help`
