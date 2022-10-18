---
layout: page
title: common/certutil (português (Brasil))
description: "Gerencie chaves e certificados em bancos de dados e tokens NSS."
content_hash: dfead994d25033d03285ba4de89bb1b522e53782
related_topics:
  - title: English version
    url: /en/common/certutil.html
    icon: bi bi-globe
---
# certutil

Gerencie chaves e certificados em bancos de dados e tokens NSS.
Mais informações: <https://manned.org/certutil>.

- Cria um novo banco de dados de certificados:

`certutil -N -d .`

- Lista todos os certificados em um banco de dados:

`certutil -L -d .`

- Lista todas as chaves privadas em um banco de dados:

`certutil -K -d . -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_senha.txt</span>

- Importa o certificado assinado para o banco de dados dos solicitantes:

`certutil -A -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_do_servidor</span>`" -t ",," -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.crt</span>` -d .`

- Adiciona nomes de assunto a um determinado certificado:

`certutil -S -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo_de_senha.txt</span>` -d . -t ",," -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">certificado_do_servidor</span>`" -n "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_servidor</span>`" -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2048</span>` -s "CN=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_comum</span>`,O=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">organização</span>`"`
