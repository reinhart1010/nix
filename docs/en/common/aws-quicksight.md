---
layout: page
title: common/aws-quicksight (English)
description: "CLI for AWS QuickSight."
content_hash: 1e251529cc26b5aba73d2af9f0fdf527ef631113
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aws-quicksight.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-quicksight.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws quicksight

CLI for AWS QuickSight.
Access QuickSight entities.
More information: <https://docs.aws.amazon.com/cli/latest/reference/quicksight/>.

- List datasets:

`aws quicksight list-data-sets --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>

- List users:

`aws quicksight list-users --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --namespace default`

- List groups:

`aws quicksight list-groups --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --namespace default`

- List dashboards:

`aws quicksight list-dashboards --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>

- Display detailed information about a dataset:

`aws quicksight describe-data-set --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_set_id</span>

- Display who has access to the dataset and what kind of actions they can perform on the dataset:

`aws quicksight describe-data-set-permissions --aws-account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_account_id</span>` --data-set-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">data_set_id</span>
