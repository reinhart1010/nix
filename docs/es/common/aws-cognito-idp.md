---
layout: page
title: common/aws-cognito-idp (español)
description: "Administra el grupo de usuarios de Amazon Cognito y sus usuarios y grupos utilizando la CLI."
content_hash: 06b7f0d487b0e3743df3ed734c62ba083f81f180
last_modified_at: 2023-04-22
related_topics:
  - title: English version
    url: /en/common/aws-cognito-idp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws cognito-idp

Administra el grupo de usuarios de Amazon Cognito y sus usuarios y grupos utilizando la CLI.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Crea un nuevo grupo de usuarios de Cognito:

`aws cognito-idp create-user-pool --pool-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista todos los grupos de usuarios:

`aws cognito-idp list-user-pools --max-results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Elimina un grupo de usuarios específico:

`aws cognito-idp delete-user-pool --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- Crea un usuario en un grupo específico:

`aws cognito-idp admin-create-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- Lista los usuarios de un pool específico:

`aws cognito-idp list-users --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>

- Elimina un usuario de un grupo específico:

`aws cognito-idp admin-delete-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user_pool_id</span>
