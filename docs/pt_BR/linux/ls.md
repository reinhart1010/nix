---
layout: page
title: linux/ls (português (Brasil))
description: "Listar o conteúdo de um diretório."
content_hash: fd9f4664ea66fde67768c9f97a4193694e65429b
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># ls

Listar o conteúdo de um diretório.
Mais informações: <https://manned.org/ls>.

- Lista um arquivo por linha:

`ls -1`

- Lista todos os arquivos, inclusive arquivos ocultos:

`ls -a`

- Liste todos os arquivos, com o separador `/` adicionado ao nome dos diretórios:

`ls -F`

- Lista longa (permissões, posse de arquivos, tamanho e data de modificação) de todos os arquivos:

`ls -la`

- Lista longa com o tamanho dos arquivos registrado de forma legível (KiB, MiB, GiB, etc.):

`ls -lh`

- Lista longa organizada por tamanho de arquivo (decrescente):

`ls -lS`

- Lista longa organizada por data de alteração (mais antigo primeiro):

`ls -ltr`

- Lista apenas diretórios:

`ls -d */`
