---
layout: page
title: common/eza (português (Brasil))
description: "Substituto moderno e mantido para o `ls`, construída sobre o `exa`."
content_hash: 0edf94f7238a69a8a1f1142f77a9d8c9938d1ee5
last_modified_at: 2024-03-02
related_topics:
  - title: English version
    url: /en/common/eza.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/eza.html
    icon: bi bi-globe
tldri18n_status: 2
---
# eza

Substituto moderno e mantido para o `ls`, construída sobre o `exa`.
Mais informações: <https://github.com/eza-community/eza>.

- Lista os arquivos um por linha:

`eza --oneline`

- Lista todos os arquivos, incluindo arquivos ocultos:

`eza --all`

- Lista no formato longo (permissões, propriedade, tamanho e data de modificação) de todos os arquivos:

`eza --long --all`

- Lista os arquivos com os maiores no topo:

`eza --reverse --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size</span>

- Exibe uma árvore de arquivos com três níveis de profundidade:

`eza --long --tree --level=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>

- Lista os arquivos ordenados pela data de modificação (mais antigos primeiro):

`eza --long --sort=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">modified</span>

- Lista os arquivos com seus cabeçalhos, ícones e status do Git:

`eza --long --header --icons --git`

- Não lista os arquivos mencionados em `.gitignore`:

`eza --git-ignore`
