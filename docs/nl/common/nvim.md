---
layout: page
title: common/nvim (Nederlands)
description: "Neovim, een programmeurs tekstbewerker gebaseerd op Vim, welke verschillende modi aanbied voor verschillende soorten text manipulatie."
content_hash: fd30399ab36fdd765d82778aed7da7cea93febcf
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/common/nvim.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/nvim.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/nvim.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/nvim.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nvim

Neovim, een programmeurs tekstbewerker gebaseerd op Vim, welke verschillende modi aanbied voor verschillende soorten text manipulatie.
Op `i` drukken in de normale modus, gaat naar de invoer modus. `<Esc>` gaat terug naar de normale modus, die geen reguliere tekst invoer accepteert.
Bekijk ook: `vim`, `vimtutor`, `vimdiff`.
Meer informatie: <https://neovim.io>.

- Open een bestand:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Ga naar de modus om tekst aan te passen (insert mode):

`<Esc>i`

- Kopieer ("yank") of knip ("delete") de huidige regel (plak het met `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Ga naar de normale modus en maak de laatste operatie ongedaan:

`<Esc>u`

- Zoek voor een patroon in het bestand (druk op `n`/`N` om naar de volgende/vorige overeenkomst te gaan):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoek_patroon</span>`<Enter>`

- Voer een reguliere expressie vervanging uit in het volledige bestand:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">vervanging</span>`/g<Enter>`

- Ga naar de normale modus, sla (write) het bestand op en sluit af:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold"><Esc>ZZ|<Esc>:wq<Enter></span>

- Sluit af zonder op te slaan:

`<Esc>:q!<Enter>`
