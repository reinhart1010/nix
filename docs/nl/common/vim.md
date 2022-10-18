---
layout: page
title: common/vim (Nederlands)
description: "Vim (Vi IMproved), een command-line tekst bewerker, geeft toegang tot verschillende manieren van tekst manipulatie."
content_hash: 3339952bd7039f4abdc4221f672c9320b46cf780
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
  - title: українська version
    url: /uk/common/vim.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/vim.html
    icon: bi bi-globe
---
# vim

Vim (Vi IMproved), een command-line tekst bewerker, geeft toegang tot verschillende manieren van tekst manipulatie.
Drukken op `i` begint invoegmodus. `<Esc>` begint normale modus, wat toegang geeft tot de Vim commando's.
Meer informatie: <https://www.vim.org>.

- Open een bestand:

`vim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Open een bestand bij een bepaald regelnummer:

`vim +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">regel_nummer</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Bekijk de handleiding van Vim:

`:help<Enter>`

- Opslaan en Afsluiten:

`:wq<Enter>`

- Maak de laatste verandering ongedaan:

`u`

- Zoek een patroon in het bestand (druk op `n`/`N` om naar de volgende/vorige overeenkomst te gaan):

`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`<Enter>`

- Voer een reguliere expressie substitutie uit in het hele bestand:

`:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervanging</span>`/g<Enter>`

- Geef de regelnummers weer:

`:set nu<Enter>`
