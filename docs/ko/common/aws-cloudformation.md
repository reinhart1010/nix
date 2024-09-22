---
layout: page
title: common/aws-cloudformation (한국어)
description: "인프라를 코드로 처리하여 AWS 및 타사 리소스를 모델링, 프로비저닝 및 관리."
content_hash: eb0921b0cbe14d4a83bb354334c1a884160d5395
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-cloudformation.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cloudformation

인프라를 코드로 처리하여 AWS 및 타사 리소스를 모델링, 프로비저닝 및 관리.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- 템플릿 파일에서 스택 생성:

`aws cloudformation create-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택-이름</span>` --region `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">지역</span>` --template-body `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file://경로/대상/파일.yml</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 스택 삭제:

`aws cloudformation delete-stack --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택-이름</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 모든 스택 나열:

`aws cloudformation list-stacks --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 실행 중인 모든 스택 나열:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 스택 상태 확인:

`aws cloudformation describe-stacks --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택-아이디</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 스택에 대한 드리프트 감지 시작:

`aws cloudformation detect-stack-drift --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택-아이디</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>

- 이전 명령어 호출 결과의 'StackDriftDetectionId'를 사용하여 스택의 드리프트 상태 출력을 확인:

`aws cloudformation describe-stack-resource-drifts --stack-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스택-드리프트-탐지-아이디</span>` --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로파일</span>
