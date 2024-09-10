---
layout: page
title: common/aws-accessanalyzer (한국어)
description: "잠재적인 보안 위험을 파악하기 위해, 리소스 정책을 분석하고 검토."
content_hash: 6c2c9a29451dfbb08b62f6d6da2aa2af3925d0f9
last_modified_at: 2024-09-10
related_topics:
  - title: English version
    url: /en/common/aws-accessanalyzer.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-accessanalyzer.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws accessanalyzer

잠재적인 보안 위험을 파악하기 위해, 리소스 정책을 분석하고 검토.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html>.

- 새로운 Access Analyzer 생성:

`aws accessanalyzer create-analyzer --analyzer-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분석기_이름</span>` --type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">타입</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">태그</span>

- 기존 Access Analyzer 삭제:

`aws accessanalyzer delete-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- 특정 Access Analyzer 세부 정보 출력:

`aws accessanalyzer get-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>

- 모든 Access Analyzers 나열:

`aws accessanalyzer list-analyzers`

- Access Analyzer 설정 업데이트:

`aws accessanalyzer update-analyzer --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --tags `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">new_tags</span>

- 새로운 Access Analyzer 아카이브 규칙 생성:

`aws accessanalyzer create-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">규칙_이름</span>` --filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filter</span>

- Access Analyzer 아카이브 규칙 삭제:

`aws accessanalyzer delete-archive-rule --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>` --rule-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rule_name</span>

- 모든 Access Analyzer 아카이브 규칙 나열:

`aws accessanalyzer list-archive-rules --analyzer-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">analyzer_arn</span>
