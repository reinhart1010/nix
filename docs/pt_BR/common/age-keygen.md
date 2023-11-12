---
layout: page
title: common/age-keygen (português (Brasil))
description: "Gera par de chaves `age`."
content_hash: 2fd0d798ac63be897d9bc079db5b8837cb305cee
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/age-keygen.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/age-keygen.html
    icon: bi bi-globe
tldri18n_status: 2
---
# age-keygen

Gera par de chaves `age`.
Veja `age` para como criptografar/descriptografar arquivos.
Mais informações: <https://manned.org/age-keygen>.

- Gera um par de chaves, salva em um arquivo não criptografado e imprime a chave pública para `stdout`:

`age-keygen --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Converte uma identidade para um destinatário e imprime a chave pública para `stdout`:

`age-keygen -y `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>
