---
layout: page
title: common/aws-sso (English)
description: "Manage access to AWS resources using Single Sign-On (SSO) credentials."
content_hash: a5f1d94853c9654491b16028d4032f7beac00aa1
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# aws sso

Manage access to AWS resources using Single Sign-On (SSO) credentials.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/index.html>.

- Start SSO session and refresh access tokens. Requires setup using `aws configure sso`:

`aws sso login`

- End SSO session and clear cached access tokens:

`aws sso logout`

- List all AWS accounts accessible to the user:

`aws sso list-accounts`

- List all roles accessible to the user for a given AWS account:

`aws sso list-account-roles --account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>

- Retrieve short-term credentials for a specific account:

`aws get-role-credentials --account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">account</span>` --role-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">token</span>
