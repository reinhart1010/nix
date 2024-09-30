---
layout: page
title: common/cdk (한국어)
description: "AWS Cloud 개발 키트 (CDK)용 CLI."
content_hash: 77bc7af585e246e98238b1438d34384a53ebb57d
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/cdk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cdk

AWS Cloud 개발 키트 (CDK)용 CLI.
더 많은 정보: <https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- 애플리케이션의 스택 나열:

`cdk ls`

- Synthesize and print the CloudFormation template for the specified stack(s):

`cdk synth `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름</span>

- 하나 이상의 스택을 배포:

`cdk deploy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름1 스택_이름2 ...</span>

- 하나 이상의 스택을 파괴:

`cdk destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름1 스택_이름2 ...</span>

- 지정된 스택을 배포된 스택 또는 로컬 CloudFormation 템플릿과 비교:

`cdk diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택_이름</span>

- 지정된 언어([l]anguage)에 대해 현재 디렉터리에 새 CDK 프로젝트를 만듬:

`cdk init -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어</span>

- 브라우저에서 CDK API 참조를 열기:

`cdk docs`
