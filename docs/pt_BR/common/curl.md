---
layout: page
title: common/curl (português (Brasil))
description: "Transfere dados entre o computador local e um servidor remoto."
content_hash: 334cc54ebd8cdd42555066d08a30c7c10731f07e
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/curl.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/curl.html
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
  - title: 中文 version
    url: /zh/common/curl.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/curl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# curl

Transfere dados entre o computador local e um servidor remoto.
Suporta a maioria dos protocolos de comunicação, incluindo HTTP, FTP e POP3.
Mais informações: <https://curl.se/docs/manpage.html>.

- Descarrega os conteúdos de um URL para um arquivo:

`curl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arquivo</span>

- Descarrega um arquivo, gravando o resultado sob o nome do arquivo indicado pelo URL:

`curl --remote-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/arquivo</span>

- Descarrega um arquivo, seguindo redirecionamentos e automaticamente continuando transferências idênticas que tenham sido interrompidas:

`curl --fail --remote-name --location --continue-at - `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/arquivo</span>

- Envia dados codificados por formulário (pedido POST do tipo `application/x-www-form-urlencoded`):

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'nome=maria'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/formulario</span>

- Envia um pedido com um cabeçalho adicional, usando um método HTTP personalizado:

`curl --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-Meu-Cabecalho: 123'</span>` --request `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PUT</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Envia dados no formato JSON, especificando o cabeçalho de tipo de conteúdo (content-type) apropriado:

`curl --data `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'{"nome":"maria"}'</span>` --header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'Content-Type: application/json'</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com/usuarios/123</span>

- Passa ao pedido o nome de usuário e senha para autenticação no servidor:

`curl --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">usuario</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- Passa ao pedido o certificado do cliente e a chave para um recurso, omitindo a validação do certificado:

`curl --cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">client.pem</span>` --key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` --insecure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
