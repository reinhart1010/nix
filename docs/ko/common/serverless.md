---
layout: page
title: common/serverless (한국어)
description: "AWS, Google Cloud, Azure 및 IBM OpenWhisk에서 서버리스 아키텍처를 배포하고 운영하기 위한 도구 모음."
content_hash: 8678f31b06b11f18c955833d423529a3f3c58e52
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/serverless.html
    icon: bi bi-globe
tldri18n_status: 2
---
# serverless

AWS, Google Cloud, Azure 및 IBM OpenWhisk에서 서버리스 아키텍처를 배포하고 운영하기 위한 도구 모음.
명령은 `serverless` 명령어 또는 그 별칭인 `sls`를 사용하여 실행할 수 있습니다.
더 많은 정보: <https://serverless.com/>.

- 서버리스 프로젝트 생성:

`serverless create`

- 템플릿에서 서버리스 프로젝트 생성:

`serverless create --template `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿_이름</span>

- 클라우드 공급자에 배포:

`serverless deploy`

- 서버리스 프로젝트 정보 표시:

`serverless info`

- 배포된 함수 호출:

`serverless invoke -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">함수_이름</span>

- 프로젝트의 로그를 실시간으로 추적:

`serverless logs -t`
