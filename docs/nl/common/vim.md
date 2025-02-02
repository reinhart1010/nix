---
layout: page
title: common/vim (Nederlands)
description: "Vim (Vi IMproved), een command-line tekst bewerker, geeft toegang tot verschillende manieren van tekst manipulatie."
content_hash: 825393149eb635d8db3c12ce5106e898dbc3c322
last_modified_at: 2024-10-15
related_topics:
  - title: Deutsch version
    url: /de/common/vim.html
    icon: bi bi-globe
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

Vim (Vi IMproved), een command-line tekst bewerker, geeft toegang tot verschillende manieren van tekst manipulatie.
Drukken op `i` begint invoegmodus. `<Esc>` begint normale modus, wat toegang geeft tot de Vim commando's.
Bekijk ook: `vimdiff`, `vimtutor` en `nvim`.
Meer informatie: <https://www.vim.org>.

- Open een bestand:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bestand bij een bepaald regelnummer:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regelnummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bekijk de handleiding van Vim:

`:help<Enter>`

- Opslaan en afsluiten:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ZZ|:wq<Enter></span>

- Terug naar normale modues en maak de laatste verandering ongedaan:

`<Esc>u`

- Zoek een patroon in het bestand (druk op `n`/`N` om naar de volgende/vorige overeenkomst te gaan):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`<Enter>`

- Voer een reguliere expressie substitutie uit in het hele bestand:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervanging</span>`/g<Enter>`

- Geef de regelnummers weer:

`:set nu<Enter>`
