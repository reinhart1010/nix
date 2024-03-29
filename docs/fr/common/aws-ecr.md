---
layout: page
title: common/aws-ecr (français)
description: "Pousse, récupère et gère les images de conteneur."
content_hash: ccfb59d3dce488aea96531fcc5bd220da2b80ef8
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/aws-ecr.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ecr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws ecr

Pousse, récupère et gère les images de conteneur.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Connecte Docker avec le registre par défaut (le nom d'utilisateur est AWS) :

`aws ecr get-login-password --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">docker login</span>` --username AWS --password-stdin `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_compte_aws</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>`.amazonaws.com`

- Crée un dépôt :

`aws ecr create-repository --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépôt</span>` --image-scanning-configuration scanOnPush=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true|false</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>

- Tag une image locale pour ECR :

`docker tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_compte_aws</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Pousse une image dans le dépôt :

`docker push `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_compte_aws</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Récupère une image depuis un dépôt :

`docker pull `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_compte_aws</span>`.dkr.ecr.`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">région</span>`.amazonaws.com/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nom_de_conteneur</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Supprime une image d'un dépôt :

`aws ecr batch-delete-image --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépôt</span>` --image-ids imageTag=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest</span>

- Supprime un dépôt :

`aws ecr delete-repository --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépôt</span>` --force`

- Liste les images dans un dépôt :

`aws ecr list-images --repository-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dépôt</span>
