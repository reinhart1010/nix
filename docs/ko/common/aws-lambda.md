---
layout: page
title: common/aws-lambda (한국어)
description: "서버를 프로비저닝하거나 관리하지 않고도 코드를 실행하기 위한 컴퓨팅 서비스인 AWS Lambda를 사용."
content_hash: fe3bf31d7b8a393bb47d908bb138e0c9a79e9e08
last_modified_at: 2024-09-25
related_topics:
  - title: English version
    url: /en/common/aws-lambda.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/aws-lambda.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-lambda.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws lambda

서버를 프로비저닝하거나 관리하지 않고도 코드를 실행하기 위한 컴퓨팅 서비스인 AWS Lambda를 사용.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/lambda/>.

- 함수 실행:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/응답.json</span>

- JSON 형식의 입력 페이로드를 사용하여 함수를 실행:

`aws lambda invoke --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --payload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/응답.json</span>

- 함수 나열:

`aws lambda list-functions`

- 함수 구성 설정을 표시:

`aws lambda get-function-configuration --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 함수 별칭 나열:

`aws lambda list-aliases --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 함수에 대해 예약된 동시성 구성 설정을 표시:

`aws lambda get-function-concurrency --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 함수를 호출할 수 있는 AWS 서비스를 나열:

`aws lambda get-policy --function-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>
