---
layout: page
title: common/dig (português (Brasil))
description: "Utilitário de pesquisa de DNS."
content_hash: 2a0201afc81f43a017a16e2847d4559653b35ad2
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/common/dig.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/dig.html
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
  - title: Türkçe version
    url: /tr/common/dig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dig

Utilitário de pesquisa de DNS.
Mais informações: <https://manned.org/dig>.

- Pesquisa o(s) IP(s) associados a um hostname (registros A):

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Obtém uma resposta detalhada para um determinado domínio (registros A):

`dig +noall +answer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Consulta um tipo de registro DNS específico associado a um nome de domínio fornecido:

`dig +short `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A|MX|TXT|CNAME|NS</span>

- Especifica um DNS alternativo para busca e opcionalmente usa DNS sobre TLS (DoT):

`dig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">+tls</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1.1.1.1|8.8.8.8|9.9.9.9|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Performa uma busca reversa de DNS em um endereço de IP (registro PTR):

`dig -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>

- Encontra servidores de nomes autorizados para a região e exibe os registros SOA:

`dig +nssearch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Performa consultas iterativas e exibe o caminho de ratreio completo para resolver um nome de domínio:

`dig +trace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- Busca um servidor DNS sobre uma [p]orta não padrão usando protocolo TCP:

`dig +tcp -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_servidor_dns</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
