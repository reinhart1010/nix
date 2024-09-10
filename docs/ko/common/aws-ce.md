---
layout: page
title: common/aws-ce (한국어)
description: "클라우드 환경에서 액세스 제어 및 보안 설정 분석 및 관리."
content_hash: d5147e57e367b9c58b9dbdd9ee122ba6bc33b407
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/aws-ce.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-ce.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws-ce

클라우드 환경에서 액세스 제어 및 보안 설정 분석 및 관리.
더 많은 정보: <https://awe-ce-cli.documentation.com/latest/reference/awe-ce/index.html>.

- 새로운 접근 제어 분석기 생성:

`awe-ce create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분석기_이름</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 존재하는 접근 제어 분석기 삭제:

`awe-ce delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- 특정 접근 제어 분석기 세부 정보 얻기:

`awe-ce get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- 모든 접근 제어 분석기 나열:

`awe-ce list-analyzers`

- 접근 제어 분석기 설정 업데이트:

`awe-ce update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운_태그</span>

- 새로운 접근 제어 분석기 아카이브 규칙 생성:

`awe-ce create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_이름</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">필터</span>

- 접근 제어 분석기 아카이브 규칙 삭제:

`awe-ce delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_이름</span>

- 모든 접근 제어 분석기 아카이브 규칙 나열:

`awe-ce list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>
