---
layout: page
title: common/aws-google-auth (português (Brasil))
description: "Linha de comando para obter credenciais (STS) temporárias AWS usando o Google Apps como um provedor (Single Sign-On) federado."
content_hash: 37f0848e4ab413d5c252593314b2462c545bd899
last_modified_at: 2023-12-28
related_topics:
  - title: Deutsch version
    url: /de/common/aws-google-auth.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-google-auth.html
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
tldri18n_status: 2
---
# aws-google-auth

Linha de comando para obter credenciais (STS) temporárias AWS usando o Google Apps como um provedor (Single Sign-On) federado.
Mais informações: <https://github.com/cevoaustralia/aws-google-auth>.

- Loga com o Google SSO usando identificadores IDP e SP e cria credenciais com duração de uma hora:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">exemplo@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Loga perguntando ([a]sking) qual papel usar (no caso de diversos papeis SAML disponíveis):

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a`

- Resolve aliases para contas AWS:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">examplo@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a --resolve-aliases`

- Exibe informações de ajuda:

`aws-google-auth -h`
