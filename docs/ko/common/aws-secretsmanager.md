---
layout: page
title: common/aws-secretsmanager (한국어)
description: "시크릿 정보 저장, 관리, 검색."
content_hash: 9fbd66f88f04ef0437376cbc19a056035616c945
last_modified_at: 2024-11-13
related_topics:
  - title: English version
    url: /en/common/aws-secretsmanager.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aws-secretsmanager.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># aws secretsmanager

시크릿 정보 저장, 관리, 검색.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 현재 계정의 시크릿 정보 관리자가 저장한 시크릿 정보를 표시:

`aws secretsmanager list-secrets`

- 시크릿 정보 생성:

`aws secretsmanager create-secret --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿_정보</span>`" --secret-string `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿</span>

- 시크릿 정보 삭제:

`aws secretsmanager delete-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>

- 시크릿 텍스트를 제외한 시크릿 세부정보 보기:

`aws secretsmanager describe-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>

- 시크릿의 정보 값을 검색 (시크릿의 최신 버전을 얻으려면 `--version-stage` 생략):

`aws secretsmanager get-secret-value --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --version-stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿_버전</span>

- Lambda 함수를 사용하여 즉시 시크릿 정보 교체:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>

- Lambda 함수를 사용하여 30일마다 자동으로 보안 암호 교체:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name_or_arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">arn_of_lambda_function</span>` --rotation-rules AutomaticallyAfterDays=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
