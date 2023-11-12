---
layout: page
title: windows/del (italiano)
description: "Cancella uno o più file."
content_hash: 366d39d20006fbe5b3243815da217837c811f124
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/windows/del.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/del.html
    icon: bi bi-globe
  - title: español version
    url: /es/windows/del.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/del.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/del.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/del.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/windows/del.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># del

Cancella uno o più file.
Maggiori informazioni: <https://learn.microsoft.com/windows-server/administration/windows-commands/del>.

- Cancella uno o più (separati da uno spazio) file o pattern:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>

- Chiedi conferma prima di cancellare ogni file:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /p`

- Forza l'eliminazione di un file a sola lettura:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /f`

- Elimina in modo ricorsivo i file da tutte le sottodirectory:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /s`

- Non chiedere conferma quando si eliminano i file in base a un carattere globale:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /q`

- Mostra il messaggio d'aiuto e fà vedere la lista di attributi disponibili:

`del /?`

- Cancella dei file in base a degli attributi specifici:

`del `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern_di_file</span>` /a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">attributo</span>
