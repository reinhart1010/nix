---
layout: page
title: common/curl (português (Brasil))
description: "Transfere dados entre o computador local e um servidor."
content_hash: df20ca225b1efc4320b5f60a6cf6c4163bf03cd4
last_modified_at: 2024-10-24
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/curl.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/curl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/curl.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/curl.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/curl.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/curl.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/curl.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/curl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

Transfere dados entre o computador local e um servidor.
Suporta a maioria dos protocolos de comunicação, incluindo HTTP, HTTPS, FTP, SCP, etc.
Mais informações: <https://curl.se/docs/manpage.html>.

- Faz um pedido HTTP GET e descarrega os conteúdos em `stdout` (saída padrão):

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Faz um pedido HTTP GET, segue redirecionamentos 3xx` e descarrega os cabeçalhos da resposta e conteúdos para `stdout`:

`curl --location --dump-header - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Baixa um arquivo, salvando a saída no arquivo indicado pela URL:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/arquivo.zip</span>

- Envia dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`). Usa `--data @file_name` ou `--data @'-'` para ler da `stdin`:

`curl -X POST --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'nome=maria'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/formulario</span>

- Envia um pedido com um cabeçalho adicional, usando um método HTTP personalizado e por meio de um proxy (tal como BurpSuite), ignorando certificados autoassinados inseguros:

`curl -k --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Authorization: Bearer token'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET|PUT|POST|DELETE|PATCH|...</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Envia dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"nome":"maria"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/usuarios/1234</span>

- Passa o certificado do cliente e chave para um recurso, pulando a validação do certificado:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cliente.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chave.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Resolve um hostname para um endereço de IP personalizado, com a saída verbosa (similar a editar o arquivo `/etc/hosts` para resolução de DNS personalizada):

`curl --verbose --resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">80</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>
