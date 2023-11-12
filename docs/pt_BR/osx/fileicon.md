---
layout: page
title: osx/fileicon (português (Brasil))
description: "Uma CLI do macOS para gerenciar ícones personalizados de arquivos e pastas."
content_hash: ace2c78c5945c8eb64e0a5e34600ff0c7ce514eb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/fileicon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fileicon

Uma CLI do macOS para gerenciar ícones personalizados de arquivos e pastas.
Mais informações: <https://github.com/mklement0/fileicon>.

- Define um ícone personalizado para um arquivo ou diretório específico:

`fileicon set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/icone.png</span>

- Remove um ícone personalizado de um arquivo ou diretório específico:

`fileicon rm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Salva o ícone personalizado de um arquivo ou diretório como um arquivo `.icns` no diretório atual:

`fileicon get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>

- Testa se um arquivo ou diretório específico tem um ícone personalizado:

`fileicon test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_ou_diretório</span>
