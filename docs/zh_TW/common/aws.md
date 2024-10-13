---
layout: page
title: common/aws (中文 (繁體, 台灣))
description: "Amazon Web Services 官方的命令列介面工具。"
content_hash: ab299df4e461a4aeb34a37d3bdfb12308aa7adf0
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
tldri18n_status: 2
---
# aws

Amazon Web Services 官方的命令列介面工具。
此命令也有關於其子命令的文件，例如：`s3`.
更多資訊：<https://aws.amazon.com/cli>.

- 設定 AWS 命令列：

`aws configure wizard`

- 使用 SSO 設定 AWS 命令​​列：

`aws configure sso`

- 取得呼叫者身分（用於排除權限問題）：

`aws sts get-caller-identity`

- 列出某個區域中的 AWS Dynamodb 並以 YAML 輸出：

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">區域</span>` --output yaml`

- 使用自動提示來幫助執行命令，：

`aws iam create-user --cli-auto-prompt`

- 取得 AWS 互動式精靈：

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">精靈名稱</span>

- 產生 JSON CLI 骨架（對於基礎設施即程式碼有用）：

`aws dynamodb update-table --generate-cli-skeleton`

- 查看 AWS 指令​​的說明：

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AWS指令</span>` help`
