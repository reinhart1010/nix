---
layout: page
title: common/aws-kendra (한국어)
description: "AWS Kendra의 CLI."
content_hash: a5c43b67b6e196f26f27828af8131fa7e54c94eb
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/common/aws-kendra.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-kendra.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws kendra

AWS Kendra의 CLI.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html>.

- 인덱스 생성:

`aws kendra create-index --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --role-arn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">role_arn</span>

- 인덱스 나열:

`aws kendra list-indexes`

- 인덱스 표시:

`aws kendra describe-index --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">index_id</span>

- 데이터 소스 나열:

`aws kendra list-data-sources`

- 데이터 소스 정보 표시:

`aws kendra describe-data-source --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_소스_아이디</span>

- 검색 쿼리 나열:

`aws kendra list-query-suggestions --index-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인덱스_아이디</span>` --query-text `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿼리_문자열</span>
