---
layout: page
title: common/aws-rds (français)
description: "CLI AWS pour Relational Database Service."
content_hash: ad0753649e6041c62dce0742a8c5da0df5222d17
related_topics:
  - title: English version
    url: /en/common/aws-rds.html
    icon: bi bi-globe
---
# aws rds

CLI AWS pour Relational Database Service.
Crée et gère des bases de données relationnelles.
Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html>.

- Affiche l'aide pour une sous-commande RDS donnée :

`aws rds `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sous_commande</span>` help`

- Stoppe une instance :

`aws rds stop-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_instance</span>

- Démarre une nouvelle instance :

`aws rds start-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_instance</span>

- Modifie une instance RDS :

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_instance</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paramètres</span>` --apply-immediately`

- Applique les mises à jour à une instance RDS :

`aws rds apply-pending-maintenance-action --resource-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_de_la_base_de_données</span>` --apply-action `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mise_à_jour_du_système</span>` --opt-in-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">immediate</span>

- Change l'identifiant d'une instance :

`aws rds modify-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ancien_identifiant_de_l_instance</span>` --new-db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nouvel_identifiant_de_l_instance</span>

- Redémarre une instance :

`aws rds reboot-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_instance</span>

- Supprime une instance :

`aws rds delete-db-instance --db-instance-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_instance</span>` --final-db-snapshot-identifier `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identifiant_de_l_image</span>` --delete-automated-backups`
