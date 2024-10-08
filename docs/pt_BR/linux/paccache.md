---
layout: page
title: linux/paccache (português (Brasil))
description: "Um utilitário de limpeza do cache do `pacman`."
content_hash: 881aa008ad1c73da2547a4f875b39072e4c56f2d
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/paccache.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paccache

Um utilitário de limpeza do cache do `pacman`.
Mais informações: <https://manned.org/paccache>.

- Remove tudo, exceto as 3 versões mais recentes do cache do `pacman`:

`paccache -r`

- Define o número de versões do pacote para manter:

`paccache -rk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">num_versoes</span>

- Executa um teste e mostra o número de pacotes candidatos para exclusão:

`paccache -d`

- Move os pacotes candidatos para um diretório ao invés de excluí-los:

`paccache -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>
