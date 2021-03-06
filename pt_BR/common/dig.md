---
layout: page
title: common/dig (português (Brasil))
description: "Utilitário de pesquisa de DNS."
content_hash: d926817e91fd9d61a540d8f9b32bd81a2f84e551
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/dig.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/dig.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/dig.html
    icon: bi bi-globe
---
# dig

Utilitário de pesquisa de DNS.
Mais informações: <https://manned.org/dig>.

- Pesquisa o(s) IP(s) associados a um hostname (Registros A):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Obtém uma resposta detalhada para um determinado domínio (Registros A):

`dig +noall +answer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Consulta um tipo de registro DNS específico associado a um nome de domínio fornecido:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>

- Obtém todos os tipos de registros para um nome de domínio fornecido:

`dig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>` ANY`

- Especifica um servidor DNS alternativo para consultar:

`dig @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Performa uma busca reversa de DNS em um endereço de IP (Registro PTR):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Encontra servidores de nomes autorizados para a região e exibe os registros SOA:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>

- Performa consultas iterativas e exibe o caminho de ratreio completo para resolver um nome de domínio:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo.com</span>
