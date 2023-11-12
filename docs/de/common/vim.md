---
layout: page
title: common/vim (Deutsch)
description: "Vim (Vi IMproved), ein Befehlszeilen-Texteditor, bietet mehrere Modi für verschiedene Arten der Textmanipulation an."
content_hash: 02a8ed96885471e1a9c51c9125ef44cc456095ef
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/vim.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/vim.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/vim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/vim.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/vim.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/vim.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/vim.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/vim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/vim.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/vim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# vim

Vim (Vi IMproved), ein Befehlszeilen-Texteditor, bietet mehrere Modi für verschiedene Arten der Textmanipulation an.
Das Drücken von `i` schaltet den Editier-Modus ein. `<Esc>` wechselt in den Befehls-Modus, der die Verwendung von Vim-Befehlen ermöglicht.
Weitere Informationen: <https://www.vim.org>.

- Öffne eine Datei:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Öffne eine Datei an einer bestimmten Zeilennummer:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zeilennummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pfad/zu/datei</span>

- Zeige Vim's Benutzeranleitung:

`:help<Enter>`

- Speichere und schließe die aktuelle Datei:

`:wq<Enter>`

- Mache die letzte Aktion rückgängig:

`u`

- Suche nach einem Muster in der Datei (mit `n`/`N` zum nächsten/vorherigen Treffer gehen):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">suchmuster</span>`<Enter>`

- Ersetze einen regulären Ausdruck alle Treffer in einer Datei:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regulärer_ausdruck</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neuer_text</span>`/g<Enter>`

- Zeige Zeilennummern an:

`:set nu<Enter>`
