---
layout: page
title: common/aws-iam (English)
description: "CLI for AWS IAM."
content_hash: 23d891837d865165e42e1ec8d943f49484172022
related_topics:
  - title: Deutsch version
    url: /de/common/aws-iam.html
    icon: bi bi-globe
---
# aws iam

CLI for AWS IAM.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Show `aws iam` help page (including all available iam commands):

`aws iam help`

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
