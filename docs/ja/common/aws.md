---
layout: page
title: common/aws (日本語)
description: "アマゾンウェブサービスの公式 CLI ツールです。"
content_hash: 6dafcc963fc303dc46dcccc220aa1b7eeb70dd3b
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
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws

アマゾンウェブサービスの公式 CLI ツールです。
`aws S3` のようないくつかのサブコマンドには、使用方法についての独自のドキュメントがあります。
詳しくはこちら: <https://aws.amazon.com/cli>.

- AWS コマンドラインを設定する:

`aws configure wizard`

- SSO を利用して AWS コマンドラインを設定する:

`aws configure sso`

- AWS コマンドのヘルプを参照する:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">コマンド</span>` help`

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
