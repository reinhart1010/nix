---
layout: page
title: common/tree (português (Brasil))
description: "Exibe o conteúdo do diretório atual em formato de árvore."
content_hash: 8c974b4f3c3e313e54b397a41d7671677066bee0
last_modified_at: 2024-05-24
related_topics:
  - title: English version
    url: /en/common/tree.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/tree.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/tree.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/common/tree.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/tree.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tree

Exibe o conteúdo do diretório atual em formato de árvore.
Mais informações: <https://manned.org/man/tree>.

- Exibe os arquivos e diretórios de acordo com o nível de profundidade 'num' informado (onde 1 significa o diretório atual):

`tree -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num</span>

- Exibe apenas diretórios:

`tree -d`

- Inclui a exibição de arquivos ocultos com colorização diferenciada:

`tree -a -C`

- Exibe a árvore sem identação, mostrando o caminho completo (usar `-N` para não escapar espaços em branco e caracteres especiais):

`tree -i -f`

- Exibe o tamanho de cada arquivo e o tamanho acumulado de cada diretório, em um formato de leitura para humanos:

`tree -s -h --du`

- Exibe arquivos em uma árvore hierárquica, utilizando um padrão coringa, e eliminando diretórios que não contêm arquivos correspondentes ao informado:

`tree -P '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`' --prune`

- Exibe diretórios em uma árvore hierárquica, utilizando um padrão coringa, e eliminando diretórios que não possuem ancestrais do informado:

`tree -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_diretorio</span>` --matchdirs --prune`

- Exibe a árvore ignorando os diretórios informados:

`tree -I '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_diretorio1|nome_diretorio2</span>`'`
