---
layout: page
title: linux/as (português (Brasil))
description: "Assembler GNU multiplataforma."
content_hash: 94be8864ed1c05e922f59eeb646bef8acf0f81f1
last_modified_at: 2024-08-13
related_topics:
  - title: Deutsch version
    url: /de/linux/as.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/as.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/as.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/as.html
    icon: bi bi-globe
tldri18n_status: 2
---
# as

Assembler GNU multiplataforma.
Seu objetivo inicial é realizar o montagem do arquivo gerado pelo `gcc` para ser utilizado pelo `ld`.
Mais informações: <https://manned.org/as>.

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado no arquivo a.out:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.s</span>

- Realiza a montagem de um arquivo, o resultado dessa operação será gravado em um arquivo específico:

`as `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.s</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/saida.o</span>

- Realiza a montagem de um arquivo rapidamente, pois ignora o pré-processamento de comentários e espaços em branco. (Deve ser utilizado apenas em compiladores confiáveis):

`as -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.s</span>

- Adiciona um caminho na lista de diretórios onde será realizada a busca por arquivos especificados na diretiva .include:

`as -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho_para_o_diretorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.s</span>
