---
layout: page
title: common/aws-configure (português (Brasil))
description: "Gerencia as configurações para o AWS CLI."
content_hash: 9c34410758d9009c8e7076f559cc23650ae692fb
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-configure.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-configure.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws-configure.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws configure

Gerencia as configurações para o AWS CLI.
Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configura interativamente o AWS CLI (cria uma nova configuração ou atualiza a configuração default):

`aws configure`

- Configura interativamente um profile para o AWS CLI (cria um novo profile ou atualiza um que já existae):

`aws configure --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_profile</span>

- Exibe o valor de uma variável específica de configuração:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>

- Exibe o valor de uma variável específica de configuração de um profile específico:

`aws configure get `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_profile</span>

- Altera o valor de uma variável específica de configuração:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>

- Altera o valor de uma variável específica de configuração de um profile específico:

`aws configure set `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_profile</span>

- Lista os entradas da configuração:

`aws configure list`

- Lista os entradas da configuração de um profile específico:

`aws configure list --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">profile_name</span>
