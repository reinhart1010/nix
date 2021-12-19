---
layout: page
title: common/aws-iam (Deutsch)
description: "CLI für AWS IAM."
content_hash: 2e67974aa743b8e9bc8d9d63319a3e7bd2630e2f
related_topics:
  - title: English version
    url: /en/common/aws-iam.html
    icon: bi bi-globe
---
# aws iam

CLI für AWS IAM.
Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Zeige die AWS IAM Hilfeseite (beinhaltet auch Hinweise für alle Unterbefehle):

`aws iam help`

- Liste aller Benutzer auf:

`aws iam list-users`

- Liste aller Richtlinien auf:

`aws iam list-policies`

- Liste aller Gruppen auf:

`aws iam list-groups`

- Liste aller Benutzer zu einer Gruppe auf:

`aws iam get-group --group-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gruppe</span>

- Liste einer IAM Richtlinie detailliert auf:

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">richtlinie</span>

- Liste alle Zugriffsschlüssel auf:

`aws iam list-access-keys`

- Liste alle Zugriffsschlüssel für einen Benutzer auf:

`aws iam list-access-keys --user-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">benutzername</span>
