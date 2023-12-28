---
layout: page
title: common/lsof (português (Brasil))
description: "Lista arquivos abertos e os seus processos correspondentes."
content_hash: 8f3786bff7758ebabdc333267d46f5e1f473df10
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/lsof.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/lsof.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lsof

Lista arquivos abertos e os seus processos correspondentes.
Nota: Privilégios de administrador (ou sudo) são necessários para listar arquivos abertos por outros.
Mais informações: <https://manned.org/lsof>.

- Localiza os processos que têm um certo arquivo aberto:

`lsof `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Localiza o processo que abriu uma porta de internet local:

`lsof -i :`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>

- Mostra o ID (PID) do processo que abriu um arquivo especificado:

`lsof -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo</span>

- Lista arquivos abertos por um certo usuário:

`lsof -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_usuario</span>

- Lista arquivos abertos por um certo comando ou processo:

`lsof -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_processo_ou_comando</span>

- Lista arquivos abertos por um certo processo, dado o seu PID:

`lsof -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Lista arquivos abertos em um diretório:

`lsof +D `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/diretório</span>

- Encontra o processo que está ouvindo uma porta de TCP local:

`lsof -iTCP:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">porta</span>` -sTCP:LISTEN`
