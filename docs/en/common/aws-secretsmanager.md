---
layout: page
title: common/aws-secretsmanager (English)
description: "Store, manage, and retrieve secrets."
content_hash: a55a95226e4591ee6fe43472b0b44c0064172d66
last_modified_at: 2024-11-13
related_topics:
  - title: 한국어 version
    url: /ko/common/aws-secretsmanager.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-secretsmanager.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws secretsmanager

Store, manage, and retrieve secrets.
More information: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- Show secrets stored by the secrets manager in the current account:

`aws secretsmanager list-secrets`

- List all secrets but only show the secret names and ARNs (easy to view):

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- Create a secret:

`aws secretsmanager create-secret --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_description</span>`" --secret-string '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>`'`

- Delete a secret (append `--force-delete-without-recovery` to delete immediately without any recovery period):

`aws secretsmanager delete-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|arn</span>

- View details of a secret except for secret text:

`aws secretsmanager describe-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|arn</span>

- Retrieve the value of a secret (to get the latest version of the secret omit `--version-stage`):

`aws secretsmanager get-secret-value --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|arn</span>` --version-stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version_of_secret</span>

- Rotate the secret immediately using a Lambda function:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>

- Rotate the secret automatically every 30 days using a Lambda function:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name|arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>` --rotation-rules AutomaticallyAfterDays=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
