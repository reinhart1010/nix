---
layout: page
title: common/aws-cognito-idp (español)
description: "Administra el grupo de usuarios de Amazon Cognito y sus usuarios y grupos utilizando la CLI."
content_hash: e828e40f7358da71136c5cdbd1baefd437eb4fd9
last_modified_at: 2024-05-22
related_topics:
  - title: Deutsch version
    url: /de/common/aws-cognito-idp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-cognito-idp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cognito-idp

Administra el grupo de usuarios de Amazon Cognito y sus usuarios y grupos utilizando la CLI.
Más información: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- Crea un nuevo grupo de usuarios de Cognito:

`aws cognito-idp create-user-pool --pool-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>

- Lista todos los grupos de usuarios:

`aws cognito-idp list-user-pools --max-results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Elimina un grupo de usuarios específico:

`aws cognito-idp delete-user-pool --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_pool</span>

- Crea un usuario en un grupo específico:

`aws cognito-idp admin-create-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_pool</span>

- Lista los usuarios de un pool específico:

`aws cognito-idp list-users --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_pool</span>

- Elimina un usuario de un grupo específico:

`aws cognito-idp admin-delete-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_usuario</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_pool</span>
