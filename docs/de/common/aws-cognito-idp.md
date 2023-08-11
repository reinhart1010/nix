---
layout: page
title: common/aws-cognito-idp (Deutsch)
description: "Verwalten des Amazon Cognito-Benutzerpools, seiner Benutzer und Gruppen mit der CLI."
content_hash: 82262e646f602fe063dd92467dc3b1891eed2670
last_modified_at: 2023-08-04
related_topics:
  - title: English version
    url: /en/common/aws-cognito-idp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cognito-idp.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws cognito-idp

Verwalten des Amazon Cognito-Benutzerpools, seiner Benutzer und Gruppen mit der CLI.
Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>

- Erstelle einen neuen Cognito-Benutzerpool:

`aws cognito-idp create-user-pool --pool-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>

- Liste alle Bentzerpools auf:

`aws cognito-idp list-user-pools --max-results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- Lösche einen bestimmten Benutzerpool:

`aws cognito-idp delete-user-pool --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzerpool_id</span>

- Erstelle einen Benutzer in einem bestimmten Pool:

`aws cognito-idp admin-create-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzerpool_id</span>

- Liste die Benutzer eines bestimmten Pool auf:

`aws cognito-idp list-users --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzerpool_id</span>

- Lösche einen  Benutzer aus einem bestimmten Pool:

`aws cognito-idp admin-delete-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzer</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzerpool_id</span>