---
layout: page
title: linux/dpkg-query (português (Brasil))
description: "Mostra informações dos pacotes instalados."
content_hash: cd6dbe63ad14ffc05c81babc43a9b1c2302b2b4d
last_modified_at: 2024-10-03
related_topics:
  - title: English version
    url: /en/linux/dpkg-query.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/dpkg-query.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dpkg-query

Mostra informações dos pacotes instalados.
Mais informações: <https://manned.org/dpkg-query.1>.

- Exibe todos os pacotes instalados:

`dpkg-query --list`

- Exibe os pacotes instalados correspondentes ao critério de busca:

`dpkg-query --list '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>`'`

- Exibe todos os arquivos instalados por um pacote:

`dpkg-query --listfiles `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Exibe informações sobre um pacote:

`dpkg-query --status `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">libc6</span>

- Busca por pacotes que contenham arquivos que correspondam ao padrão:

`dpkg-query --search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/ld.so.conf.d</span>
