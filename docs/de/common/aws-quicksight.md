---
layout: page
title: common/aws-quicksight (Deutsch)
description: "CLI für AWS QuickSight."
content_hash: eaa7a29ecbaed7e77c05df9a17e91289964aded7
related_topics:
  - title: English version
    url: /en/common/aws-quicksight.html
    icon: bi bi-globe
---
# aws quicksight

CLI für AWS QuickSight.
Weitere Informationen: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- Liste alle Datensätze auf:

`aws quicksight list-data-sets --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>

- Liste alle Benutzer auf:

`aws quicksight list-users --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --namespace default`

- Liste alle Gruppen auf:

`aws quicksight list-groups --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --namespace default`

- Liste alle Dashboards auf:

`aws quicksight list-dashboards --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>

- Liste einen Datensatz detailliert aus:

`aws quicksight describe-data-set --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datensatz_id</span>

- Liste Zugangsberechtigungen zu einem Datensatz auf:

`aws quicksight describe-data-set-permissions --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">datensatz_id</span>
