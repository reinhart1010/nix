---
layout: page
title: common/aws (Deutsch)
description: "Das offizielle CLI für Amazon Web Services."
content_hash: 2c8745953e94f491c1f882f291f98167dca14a71
last_modified_at: 2023-11-12
related_topics:
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
  - title: polski version
    url: /pl/common/aws.html
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

Das offizielle CLI für Amazon Web Services.
Manche Unterbefehle wie `aws s3` sind separat dokumentiert.
Weitere Informationen: <https://aws.amazon.com/cli>.

- Konfiguriere die AWS Kommandozeile:

`aws configure wizard`

- Konfiguriere die AWS Kommandozeile mithilfe von SSO:

`aws configure sso`

- Zeige Hilfe für ein Kommando an:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">befehl</span>` help`

- Zeige Informationen über die eigene angenommene Identität (häufig benutzt zur Fehlersuche):

`aws sts get-caller-identity`

- Liste alle AWS Ressourcen in einer Region mit YAML Formatierung auf:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- Erstelle einen IAM Benutzer mit Ausführungsassistent:

`aws iam create-user --cli-auto-prompt`

- Öffne einen Assistenten für eine AWS Ressource:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">neue_tabelle</span>

- Erstelle einen JSON CLI-Aufbau (hilfreich für Infrastruktur-Automation):

`aws dynamodb update-table --generate-cli-skeleton`
