---
layout: page
title: common/nvim (Nederlands)
description: "Neovim, een programmeurs tekstbewerker gebaseerd op Vim, welke verschillende modi aanbied voor verschillende soorten text manipulatie."
content_hash: a4111e09cd269f2e03309ea884a6a6385a9f3c9e
last_modified_at: 2023-11-26
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nvim.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nvim

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

`<Esc>:wq<Enter>`

- Sluit af zonder op te slaan:

`<Esc>:q!<Enter>`
