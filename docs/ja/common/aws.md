---
layout: page
title: common/aws (日本語)
description: "アマゾンウェブサービスの公式 CLI ツールです。"
content_hash: 4636d8f5146aa75f9baa17a807748dcb17ad03fd
last_modified_at: 2024-10-13
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

アマゾンウェブサービスの公式 CLI ツールです。
`s3` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
詳しくはこちら: <https://aws.amazon.com/cli>

- AWS コマンドラインを設定する:

`aws configure wizard`

- SSO を利用して AWS コマンドラインを設定する:

`aws configure sso`

- 操作呼び出しに使用した認証情報の取得（パーミッションのトラブルシューティングに使用します）:

`aws sts get-caller-identity`

- リージョン内の AWS リソースをリストアップし、YAML で出力する:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- 自動プロンプトを使用してコマンドを補助する:

`aws iam create-user --cli-auto-prompt`

- AWS リソースの対話型ウィザードを取得する:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">新しいテーブル</span>

- JSON CLI スケルトンを生成する（Infrastructure as Code に役立ちます）:

`aws dynamodb update-table --generate-cli-skeleton`

- AWS コマンドのヘルプを参照する:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>` help`
