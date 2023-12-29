---
layout: page
title: common/vimdiff (Deutsch)
description: "Öffne zwei oder mehr Dateien in Vim und zeige ihre Unterschiede an."
content_hash: 99be8d7606d01b80b8b3e2df3529fb39f4b092bc
last_modified_at: 2023-12-29
related_topics:
  - title: English version
    url: /en/common/vimdiff.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vimdiff.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vimdiff.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vimdiff

Öffne zwei oder mehr Dateien in Vim und zeige ihre Unterschiede an.
Siehe auch `vim`.
Weitere Informationen: <https://www.vim.org>.

- Öffne zwei Dateien und zeige ihre Unterschiede an:

`vimdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei_2</span>

- Bewege den Cursor zum linken|rechten Fenster:

`<Ctrl> + w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">h|l</span>

- Springe zum vorigen Unterschied:

`[c`

- Springe zum nächsten Unterschied:

`]c`

- Kopiere die hervorgehobenen Unterschiede vom anderen in das aktuelle Fenster:

`do`

- Kopiere die hervorgehobenen Unterschiede vom aktuellen in das andere Fenster:

`dp`

- Aktualisiere die hervorgehobenen Unterschiede und Textfaltungen:

`:diffupdate`

- Öffne/Schließe die Textfaltung unter dem Cursor:

`za`
