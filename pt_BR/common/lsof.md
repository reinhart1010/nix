---
layout: page
title: common/lsof (português (Brasil))
description: "Lista arquivos abertos e os seus processos correspondentes."
content_hash: 01c9c955f0d555149678c92a93e8344015c6848e
related_topics:
  - title: English version
    url: /en/common/lsof.html
    icon: bi bi-globe
---
# lsof

Lista arquivos abertos e os seus processos correspondentes.
Nota: Privilégios de administrador (ou sudo) são necessários para listar arquivos abertos por outros.
Mais informações: <https://manned.org/lsof>.

- Localizar os processos que têm um certo arquivo aberto:

`lsof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Localizar o processo que abriu uma porta de internet local:

`lsof -i :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Mostrar o ID (PID) do processo que abriu um arquivo especificado:

`lsof -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Listar arquivos abertos por um certo usuário:

`lsof -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_usuario</span>

- Listar arquivos abertos por um certo comando ou processo:

`lsof -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_processo_ou_comando</span>

- Listar arquivos abertos por um certo processo, dado o seu PID:

`lsof -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Listar arquivos abertos em um diretório:

`lsof +D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Encontrar o processo que está ouvindo uma porta de TCP local:

`lsof -iTCP:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` -sTCP:LISTEN`
