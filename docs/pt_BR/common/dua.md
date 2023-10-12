---
layout: page
title: common/dua (português (Brasil))
description: "Dua (Analisador de Uso de Disco) é uma ferramenta para análise conveniente do uso de disco dado um diretório."
content_hash: 78fcb25afd0057179f79bf2cfe036cd889657c67
last_modified_at: 2023-10-12
related_topics:
  - title: English version
    url: /en/common/dua.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># dua

Dua (Analisador de Uso de Disco) é uma ferramenta para análise conveniente do uso de disco dado um diretório.
Mais informações: <https://github.com/Byron/dua-cli>.

- Analisa um diretório específico:

`dua `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretorio}`

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
