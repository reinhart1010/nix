---
layout: page
title: linux/locate (português (Brasil))
description: "Encontre nomes de arquivos rapidamente."
content_hash: 982fa6d3821bb5c360a90df84cf0fbe2fb105c4a
last_modified_at: 2024-01-10
related_topics:
  - title: Deutsch version
    url: /de/linux/locate.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/locate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# locate

Encontre nomes de arquivos rapidamente.
Mais informações: <https://manned.org/locate>.

- Procura por padrões no banco de dados. Nota: o banco de dados é recalculado periodicamente (geralmente semanalmente ou diariamente):

`locate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">padrão</span>

- Procura um arquivo pelo seu nome de arquivo exato(um padrão que não contém caracteres curingas é interpretado como `*pattern*`):

`locate '*/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_arquivo</span>`'`

- Recalcula o banco de dados. Você precisa fazer se você quiser achar os arquivos recentementes adicionados:

`sudo updatedb`
