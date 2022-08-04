---
layout: page
title: common/aws (polski)
description: "Oficjalne narzędzie CLI dla Amazon Web Services."
content_hash: 640259ef7198095a61a4eef26b7d532e9811abc7
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
---
# aws

Oficjalne narzędzie CLI dla Amazon Web Services.
Wizard, SSO, Resource Autocompletion, i opcje YAML są tylko v2.
Więcej informacji: <https://aws.amazon.com/cli>.

- Konfiguruj AWS Command-line:

`aws configure wizard`

- Konfiguruj AWS Command-line używając SSO:

`aws configure sso`

- Zobacz tekst pomocy dla polecenia AWS:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` help`

- Uzyskaj tożsamość wywołującego (służy do rozwiązywania problemów z uprawnieniami):

`aws sts get-caller-identity`

- Wyświetla listę zasobów AWS w regionie i wyświetla w yaml:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Użyj auto prompt do pomocy z poleceniem:

`aws iam create-user --cli-auto-prompt`

- Uzyskaj interaktywnego kreatora dla zasobu AWS:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowa_tabela</span>

- Generuj JSON CLI Skeleton (przydatne dla infrastruktury jako kodu):

`aws dynamodb update-table --generate-cli-skeleton`
