---
layout: page
title: common/aws (polski)
description: "Oficjalne narzędzie CLI dla Amazon Web Services."
content_hash: c3f84268366eca256a656238b0c4d94be649bea7
last_modified_at: 2024-06-23
related_topics:
  - title: Deutsch version
    url: /de/common/aws.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/aws.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/aws.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/aws.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/aws.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws

Oficjalne narzędzie CLI dla Amazon Web Services.
Niektóre podkomendy takie jak `aws s3` mają osobną dokumentację.
Więcej informacji: <https://aws.amazon.com/cli>.

- Konfiguruj AWS Command-line:

`aws configure wizard`

- Konfiguruj AWS Command-line używając SSO:

`aws configure sso`

- Uzyskaj tożsamość wywołującego (służy do rozwiązywania problemów z uprawnieniami):

`aws sts get-caller-identity`

- Uzyskaj listę zasobów AWS w regionie i wyświetl ją w YAML:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Użyj auto prompt do pomocy z poleceniem:

`aws iam create-user --cli-auto-prompt`

- Uzyskaj interaktywnego kreatora dla zasobu AWS:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nowa_tabela</span>

- Generuj JSON CLI Skeleton (przydatne dla infrastruktury jako kodu):

`aws dynamodb update-table --generate-cli-skeleton`

- Wyświetl pomoc dla określonej komendy:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">komenda</span>` help`
