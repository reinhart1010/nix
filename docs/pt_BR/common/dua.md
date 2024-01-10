---
layout: page
title: common/dua (português (Brasil))
description: "Dua (Analisador de Uso de Disco) é uma ferramenta para análise conveniente do uso de disco dado um diretório."
content_hash: bdcfda67222e27339c46fc10ad5c30a0427d860c
last_modified_at: 2024-01-10
related_topics:
  - title: English version
    url: /en/common/dua.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dua

Dua (Analisador de Uso de Disco) é uma ferramenta para análise conveniente do uso de disco dado um diretório.
Mais informações: <https://github.com/Byron/dua-cli>.

- Analisa um diretório específico:

`dua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio</span>

- Exibe o tamanho aparente ao invés do uso do disco:

`dua --apparent-size`

- Contabiliza arquivos hard-linked cada vez que eles são encontrados:

`dua --count-hard-links`

- Agrega o espaço em disco consumido de um ou mais diretórios ou arquivos:

`dua aggregate`

- Inicia a interface de usuário:

`dua interactive`

- Seleciona o formato para contagem de bytes:

`dua --format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">metric|binary|bytes|GB|GiB|MB|MiB</span>

- Escolhe o número de threads a serem usadas:

`dua --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">numero</span>
