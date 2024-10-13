---
layout: page
title: common/aws (français)
description: "La CLI officielle pour Amazon Web Services."
content_hash: facfb3b3a0f64196c73cde6234ce6bf33c13b339
last_modified_at: 2024-10-13
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/aws.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws

La CLI officielle pour Amazon Web Services.
Certaines commandes comme `aws s3` ont leur propre documentation.
Plus d'informations : <https://aws.amazon.com/cli>.

- Configure la ligne de commande AWS :

`aws configure wizard`

- Configure la ligne de commande AWS en utilisant le SSO :

`aws configure sso`

- Récupère l'identité de l'appelant (utilisé pour débogguer les permissions) :

`aws sts get-caller-identity`

- Liste les ressources AWS d'une région et affiche le résultat en YAML :

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Utilise l'aide automatique au remplissage d'une commande :

`aws iam create-user --cli-auto-prompt`

- Utilise un guide interactif pour une ressource AWS :

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouvelle_table</span>

- Génère un squelette CLI en JSON (utile pour l'Infrastructure as Code) :

`aws dynamodb update-table --generate-cli-skeleton`

- Voir l'aide pour une commande AWS :

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commande</span>` help`
