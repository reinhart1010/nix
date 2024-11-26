---
layout: page
title: common/aws-secretsmanager (한국어)
description: "시크릿을 저장, 관리 및 검색."
content_hash: 1a13bbdba62f4b458c1a713fdca92d591a3fa043
last_modified_at: 2024-11-26
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

시크릿을 저장, 관리 및 검색.
더 많은 정보: <https://docs.aws.amazon.com/cli/latest/reference/secretsmanager/>.

- 현재 계정에 저장된 시크릿 표시:

`aws secretsmanager list-secrets`

- 모든 시크릿 표시 (시크릿 이름 및 ARN만 표시, 보기 쉬움):

`aws secretsmanager list-secrets --query 'SecretList[*].{Name: Name, ARN: ARN}'`

- 시크릿 생성:

`aws secretsmanager create-secret --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --description "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿_설명</span>`" --secret-string '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿</span>`'`

- 시크릿 삭제 (복구 없이 즉시 삭제하려면 `--force-delete-without-recovery` 추가):

`aws secretsmanager delete-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|arn</span>

- 시크릿 세부 정보 표시 (시크릿 텍스트 제외):

`aws secretsmanager describe-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|arn</span>

- 시크릿 값 검색 (최신 버전의 시크릿을 얻으려면 `--version-stage` 생략):

`aws secretsmanager get-secret-value --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|arn</span>` --version-stage `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">시크릿_버전</span>

- 즉시 시크릿 교체을 위해 람다 함수 사용:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">람다_함수_arn</span>

- 30일마다 자동으로 시크릿 교체을 위해 람다 함수 사용:

`aws secretsmanager rotate-secret --secret-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름|arn</span>` --rotation-lambda-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">람다_함수_arn</span>` --rotation-rules AutomaticallyAfterDays=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">30</span>
