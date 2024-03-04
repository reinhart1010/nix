---
layout: page
title: common/aws-iam (English)
description: "Intecract with the Identity and Access Management (IAM), a web service for securely controlling access to AWS services."
content_hash: 8ab8df18b2991fba6e26e4539ddab971bb684029
last_modified_at: 2024-03-04
related_topics:
  - title: Deutsch version
    url: /de/common/aws-iam.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-iam.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-iam.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws iam

Intecract with the Identity and Access Management (IAM), a web service for securely controlling access to AWS services.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- List users:

`aws iam list-users`

- List policies:

`aws iam list-policies`

- List groups:

`aws iam list-groups`

- Get users in a group:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">group_name</span>

- Describe an IAM policy:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">policy_name</span>

- List access keys:

`aws iam list-access-keys`

- List access keys for a specific user:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_name</span>

- Display help:

`aws iam help`
