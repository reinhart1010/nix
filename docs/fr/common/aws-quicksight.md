---
layout: page
title: common/aws-quicksight (français)
description: "CLI pour AWS QuickSight."
content_hash: 112068a19e6be10b7565f48e12b961b4a1ec90c6
last_modified_at: 2023-12-20
related_topics:
  - title: Deutsch version
    url: /de/common/aws-quicksight.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-quicksight.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws quicksight

CLI pour AWS QuickSight.
Accès aux entrées QuickSight.
Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Liste les datasets :

`aws quicksight list-data-sets --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>

- Liste les utilisateurs :

`aws quicksight list-users --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>` --namespace default`

- Liste les groupes :

`aws quicksight list-groups --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>` --namespace default`

- Liste les tableaux de bords :

`aws quicksight list-dashboards --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>

- Affiche les informations détaillées sur un dataset :

`aws quicksight describe-data-set --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_data_set</span>

- Affiche les personnes qui peuvent accéder au dataset et quelles actions ils peuvent effectuer sur ce dernier :

`aws quicksight describe-data-set-permissions --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_compte_aws</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">id_data_set</span>
