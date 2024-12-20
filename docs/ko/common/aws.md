---
layout: page
title: common/aws (한국어)
description: "Amazon Web Services의 공식 CLI tool입니다."
content_hash: 01750b246ac05964df9cf5223405fe6db0f2474b
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

Amazon Web Services의 공식 CLI tool입니다.
`s3`와 같은 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://aws.amazon.com/cli>.

- AWS Command-line 설정:

`aws configure wizard`

- SSO를 사용해 AWS Command-line 설정:

`aws configure sso`

- 호출자 ID 가져오기 (권한 문제 해결에 사용됨):

`aws sts get-caller-identity`

- 지역의 AWS 리소스 목록 및 YAML로 출력:

`aws dynamodb list-tables --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-east-1</span>` --output yaml`

- 명령에 대한 자동 프롬프트 사용:

`aws iam create-user --cli-auto-prompt`

- AWS 리소스에 대한 대화형 마법사 사용:

`aws dynamodb wizard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_table</span>

- JSON CLI 스켈레톤 생성 (인프라를 코드로 사용하는 데 유용):

`aws dynamodb update-table --generate-cli-skeleton`

- AWS 명령에 대한 도움말:

`aws `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>` help`
