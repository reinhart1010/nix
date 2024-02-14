---
layout: page
title: common/aws-quicksight (English)
description: "Create, delete, list, search and update AWS QuickSight entities."
content_hash: 98a844e95f244e6c4222684303b8912584f4f7ee
last_modified_at: 2024-02-14
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

Create, delete, list, search and update AWS QuickSight entities.
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
