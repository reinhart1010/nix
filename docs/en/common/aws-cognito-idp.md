---
layout: page
title: common/aws-cognito-idp (English)
description: "Configure an Amazon Cognito user pool and its users and groups and authenticate them."
content_hash: 99c2560578803d1d87e05a0ca02f4f571d579135
last_modified_at: 2024-03-04
related_topics:
  - title: Deutsch version
    url: /de/common/aws-cognito-idp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cognito-idp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cognito-idp

Configure an Amazon Cognito user pool and its users and groups and authenticate them.
More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Create a new Cognito user pool:

`aws cognito-idp create-user-pool --pool-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- List all user pools:

`aws cognito-idp list-user-pools --max-results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Delete a specific user pool:

`aws cognito-idp delete-user-pool --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- Create a user in a specific pool:

`aws cognito-idp admin-create-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- List the users of a specific pool:

`aws cognito-idp list-users --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- Delete a user from a specific pool:

`aws cognito-idp admin-delete-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>
