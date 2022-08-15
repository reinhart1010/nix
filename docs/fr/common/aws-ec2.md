---
layout: page
title: common/aws-ec2 (français)
description: "CLI pour AWS EC2."
content_hash: b1eb4a386fb11081ed9ace345f44edaa6b799a3f
related_topics:
  - title: Deutsch version
    url: /de/common/aws-ec2.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-ec2.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-ec2.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws ec2

CLI pour AWS EC2.
Provisionne, sécurise et des capacités de calcul redimensionnable dans le cloud AWS pour accélérer le développement et le déploiement d'applications.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Affiche la liste de toutes les commandes EC2 disponible :

`aws ec2 help`

- Affiche l'aide pour une sous-commande EC2 spécifique :

`aws ec2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sous-commande</span>` help`

- Affiche les informations sur une instance spécifique :

`aws ec2 describe-instances --instance-ids `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_d_instance</span>

- Affiche les informations de toutes les instances :

`aws ec2 describe-instances`

- Affiche les informations sur tous les volumes EC2 :

`aws ec2 describe-volumes`

- Supprime un volume EC2 :

`aws ec2 delete-volume --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_volume</span>

- Crée une sauvegarde de votre volume EC2 :

`aws ec2 create-snapshot --volume-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_de_volume</span>

- Liste toutes les AMIs (Images de Machine Amazon) disponible :

`aws ec2 describe-images`
