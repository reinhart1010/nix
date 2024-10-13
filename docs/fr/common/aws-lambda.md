---
layout: page
title: common/aws-lambda (français)
description: "CLI pour AWS lambda."
content_hash: 034f854e7e0004df5388c75391a4aebfb6a0a5c8
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/aws-lambda.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-lambda.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lambda

CLI pour AWS lambda.
Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- Lance une fonction :

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la/réponse.json</span>

- Lance une fonction avec pour donnée d'entrée, un document JSON :

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/la/réponse.json</span>

- Liste les fonctions :

`aws lambda list-functions`

- Affiche la configuration d'une fonction :

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Affiche les alias d'une fonction :

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Affiche la configuration de concurrence pour une fonction :

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>

- Affiche quel service AWS peut appeler une fonction :

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom</span>
