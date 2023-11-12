---
layout: page
title: common/aws-ses (português (Brasil))
description: "Interface de linha de comando para o AWS Simple Email Service."
content_hash: 0a4e27863a37c65ddad39aa95b0c14e950f73b12
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/aws-ses.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ses

Interface de linha de comando para o AWS Simple Email Service.
Serviço em nuvem com alta performance para envio e recebimento de emails.
Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- Cria um novo conjunto de regras:

`aws ses create-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_conjunto_de_regras</span>` --generate-cli-skeleton`

- Descreve os conjuntos ativos de regras:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- Descreve um regra específica de um conjunto de regras:

`aws ses describe-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_conjunto_de_regras</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_regra</span>` --generate-cli-skeleton`

- Lista todos os conjuntos de regras:

`aws ses list-receipt-rule-sets --starting-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">texto_do_token</span>` --max-items `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">inteiro</span>` --generate-cli-skeleton`

- Remove um conjunto de regras específico (o conjunto ativo não pode ser removido):

`aws ses delete-receipt-rule-set --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_conjunto_de_regras</span>` --generate-cli-skeleton`

- Remove uma regras específica de um conjunto de regras:

`aws ses delete-receipt-rule --rule-set-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_do_conjunto_de_regras</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_da_regra</span>` --generate-cli-skeleton`

- Envia um email:

`aws ses send-email --from `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">de_endereco</span>` --destination "ToAddresses=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">para_endereco</span>`" --message "Subject={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">assunto</span>`,Charset=utf8},Body={Text={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">corpo_email</span>`,Charset=utf8},Html={Data=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">corpo_do_email_com_html</span>`,Charset=utf8</span>`"`

- Exibe ajuda para um subcomando específico do SES:

`aws ses `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">subcomando</span>` help`
