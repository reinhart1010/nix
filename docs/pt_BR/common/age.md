---
layout: page
title: common/age (português (Brasil))
description: "Uma simples, moderna e segura ferramenta de criptografia de arquivos."
content_hash: f4505f82ae5b98ee873f6a9b418170ee380660c7
last_modified_at: 2023-11-12
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
  - title: italiano version
    url: /it/common/age.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/age.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># age

Uma simples, moderna e segura ferramenta de criptografia de arquivos.
Mais informações: <https://github.com/FiloSottile/age>.

- Gera um arquivo criptografado que pode ser descriptografado com uma frase-chave:

`age --passphrase --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>

- Gera um par de chaves, salvando a chave privada em um arquivo não criptografado e imprimindo a chave pública para `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Criptografa arquivo com uma ou mais chaves públicas que são inseridas como literais:

`age --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave_pública_1</span>` --recipient `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave_pública_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>

- Criptografa arquivo com uma ou mais chaves públicas que são especificadas no arquivo do destinatário:

`age --recipients-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_destinatário</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>

- Descriptografa um arquivo com uma frase-chave:

`age --decrypt --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>

- Descriptografa um arquivo com um arquivo chave privada:

`age --decrypt --identity `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_chave_privada</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_descriptografado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_criptografado</span>
