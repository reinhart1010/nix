---
layout: page
title: osx/hdiutil (português (Brasil))
description: "Utilitário para criar e gerenciar imagens de disco."
content_hash: 4eb048b9498ce841ba2b76d0ae19740f33a891e2
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/hdiutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdiutil

Utilitário para criar e gerenciar imagens de disco.
Mais informações: <https://keith.github.io/xcode-man-pages/hdiutil.1.html>.

- Monta uma imagem:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/aquivo_de_imagem</span>

- Desmonta uma imagem:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Lista as imagens montadas:

`hdiutil info`

- Cria uma imagem ISO a partir do conteúdo de um diretório:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_saída</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
