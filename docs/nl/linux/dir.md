---
layout: page
title: linux/dir (Nederlands)
description: "Toon de inhoud van een directory met één regel per bestand, speciale tekens worden weergegeven met backslash-escape-sequenties."
content_hash: 0dcc7f9fff0e7607b81460a71ac11e3f75b82d19
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/linux/dir.html
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

- Toon hulp:

`dir --help`
