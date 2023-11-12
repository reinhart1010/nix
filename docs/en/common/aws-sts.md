---
layout: page
title: common/aws-sts (English)
description: "Security Token Service (STS) allows to request temporary credentials for (IAM) users or federated users."
content_hash: eaf36988281fa7c1db0ac6cdf2e920f0eed65052
last_modified_at: 2023-11-12
related_topics:
  - title: português (Brasil) version
    url: /pt_BR/common/aws-sts.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sts

Security Token Service (STS) allows to request temporary credentials for (IAM) users or federated users.
More information: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Get temporary security credentials to access specific AWS resources:

`aws sts assume-role --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">aws_role_arn</span>

- Get an IAM user or role whose credentials are used to call the operation:

`aws sts get-caller-identity`
