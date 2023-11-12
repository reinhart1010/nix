---
layout: page
title: osx/hdiutil (português (Brasil))
description: "Utilitário para criar e gerenciar imagens de disco."
content_hash: f7b0c2bba36aa5f9d6519649704ff346fdc81570
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/hdiutil.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hdiutil

Utilitário para criar e gerenciar imagens de disco.
Mais informações: <https://ss64.com/osx/hdiutil.html>.

- Monta uma imagem:

`hdiutil attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/aquivo_de_imagem</span>

- Desmonta uma imagem:

`hdiutil detach /Volumes/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_volume</span>

- Lista as imagens montadas:

`hdiutil info`

- Cria uma imagem ISO a partir do conteúdo de um diretório:

`hdiutil makehybrid -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_saída</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>
