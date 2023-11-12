---
layout: page
title: common/aws-google-auth (English)
description: "Command-line tool to acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider."
content_hash: b3690e69a3d7c17a321253779cbe79a0b44f5629
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/common/aws-google-auth.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-google-auth.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-google-auth.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws-google-auth.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-google-auth.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws-google-auth

Command-line tool to acquire AWS temporary (STS) credentials using Google Apps as a federated (Single Sign-On) provider.
More information: <https://github.com/cevoaustralia/aws-google-auth>.

- Log in with Google SSO using the IDP and SP identifiers and set the credentials duration to one hour:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Log in [a]sking which role to use (in case of several available SAML roles):

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a`

- Resolve aliases for AWS accounts:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a --resolve-aliases`

- Show help information:

`aws-google-auth -h`
