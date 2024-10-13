---
layout: page
title: common/aws-iam (Deutsch)
description: "CLI für AWS IAM."
content_hash: e0809d9373aeff265e0127a53f938777bc8e9202
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/aws-iam.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-iam.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-iam.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-iam.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-iam.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws iam

CLI für AWS IAM.
Weitere Informationen: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

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

- Zeige die AWS IAM Hilfeseite (beinhaltet auch Hinweise für alle Unterbefehle):

`aws iam help`
