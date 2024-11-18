---
layout: page
title: common/age (português (Brasil))
description: "Uma simples, moderna e segura ferramenta de criptografia de arquivos."
content_hash: 93a99a94c68276a361a7b27df049eef440717bf5
last_modified_at: 2024-11-18
related_topics:
  - title: Deutsch version
    url: /de/common/age.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/age.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/age.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/age.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/age.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/age.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age

Uma simples, moderna e segura ferramenta de criptografia de arquivos.
Veja também: `age-keygen` para geração de pares de chaves.
Mais informações: <https://github.com/FiloSottile/age>.

- Gera um arquivo criptografado que pode ser descriptografado com uma frase-chave:

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>

- Criptografa arquivo com uma ou mais chaves públicas que são inseridas como literais (repita o argumento `--recipient` para especificar múltiplas chaves públicas):

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave_pública</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>

- Criptografa arquivo com um ou mais destinatários que são especificadas em um arquivo (um por linha):

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_destinatários</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>

- Descriptografa um arquivo com uma frase-chave:

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>

- Descriptografa um arquivo com um arquivo de chave privada:

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_chave_privada</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>
