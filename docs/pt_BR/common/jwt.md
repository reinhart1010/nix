---
layout: page
title: common/jwt (português (Brasil))
description: "Uma ferramenta de linha de comando (command-line tool) para trabalhar com JSON Web Tokens (JWTs)."
content_hash: 180c298135c9a3a7aeda980f9d3f1f21f62f0fea
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/jwt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jwt

Uma ferramenta de linha de comando (command-line tool) para trabalhar com JSON Web Tokens (JWTs).
Algoritmos de encriptação disponíveis são HS256, HS384, HS512, RS256, RS384, RS512, ES256, ES384.
Mais informações: <https://github.com/mike-engel/jwt-cli>.

- Decodifica um JWT:

`jwt decode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_string</span>

- Decodifica um JWT em uma JSON string:

`jwt decode -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jwt_string</span>

- Codifica uma JSON string em um JWT:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json_string</span>`'`

- Codifica dados (payload) de um par de chaves (key pair) em um JWT:

`jwt encode --alg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">HS256</span>` --secret `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234567890</span>` -P chave=valor`
