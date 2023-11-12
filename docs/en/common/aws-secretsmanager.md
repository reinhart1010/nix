---
layout: page
title: common/aws-secretsmanager (English)
description: "Store, manage, and retrieve secrets."
content_hash: 26b08e62e6cd54ab203e3fb840fdd6d4bcc5a3c8
last_modified_at: 2023-11-12
related_topics:
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

- Create a secret:

`aws secretsmanager create-secret --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret_description</span>`" --secret-string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">secret</span>

- Delete a secret:

`aws secretsmanager delete-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>

- View details of a secret except for secret text:

`aws secretsmanager describe-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>

- Retrieve the value of a secret (to get the latest version of the secret omit `--version-stage`):

`aws secretsmanager get-secret-value --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --version-stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">version_of_secret</span>

- Rotate the secret immediately using a Lambda function:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>

- Rotate the secret automatically every 30 days using a Lambda function:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>` --rotation-rules AutomaticallyAfterDays=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
