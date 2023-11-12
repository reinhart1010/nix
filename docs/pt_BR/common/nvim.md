---
layout: page
title: common/nvim (português (Brasil))
description: "Neovim, um editor de texto para programadores baseado no Vim, oferece vários modos para diferentes tipos de manipulação de texto."
content_hash: 2a478e9a539e07deb1199ef15132aab3dc6206fc
last_modified_at: 2023-11-12
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
tldri18n_status: 2
---
# nvim

Neovim, um editor de texto para programadores baseado no Vim, oferece vários modos para diferentes tipos de manipulação de texto.
Pressionar`i` no modo normal entra no modo de inserção. `<Esc>` retorna ao modo normal, que não permite a inserção regular de texto.
Veja também `vim`, `vimtutor`, `vimdiff`.
Mais informações: <https://neovim.io>.

- Abre um arquivo:

`nvim `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Entra no modo de edição de texto (mode de inserção):

`<Esc>i`

- Copia ("yank") ou recorta ("delete") a linha atual (cole-a com `P`):

`<Esc>`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">yy|dd</span>

- Entra no modo normal e desfaz a última operação:

`<Esc>u`

- Procura por um padrão em um arquivo (pressione `n`/ `N` para ir para a próxima/prévia correspondência):

`<Esc>/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão_procurado</span>`<Enter>`

- Executa uma substituição de expressão regular em todo o arquivo:

`<Esc>:%s/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressão_regular</span>`/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">substituição</span>`/g<Enter>`

- Entra no modo normal, salva (grava) o arquivo e sai:

`<Esc>:wq<Enter>`

- Sai sem salvar:

`<Esc>:q!<Enter>`
