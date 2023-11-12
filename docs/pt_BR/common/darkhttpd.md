---
layout: page
title: common/darkhttpd (português (Brasil))
description: "Servidor web Darkhttpd."
content_hash: 8f8245d4e0e0584dbcad4b546411059aa986424a
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/darkhttpd.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/darkhttpd.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/darkhttpd.html
    icon: bi bi-globe
tldri18n_status: 2
---
# darkhttpd

Servidor web Darkhttpd.
Mais informações: <https://unix4lyfe.org/darkhttpd>.

- Inicia o servidor servindo a raiz do documento especificada:

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/raiz_do_documento</span>

- Inicia o servidor na porta especificada (porta 8080 por padrão se estiver executando como usuário não raiz):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/raiz_do_documento</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Escuta apenas no endereço IP especificado (por padrão, o servidor escuta em todas as interfaces):

`darkhttpd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/raiz_do_documento</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">endereço_de_ip</span>
