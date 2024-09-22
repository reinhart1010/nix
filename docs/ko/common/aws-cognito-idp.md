---
layout: page
title: common/aws-cognito-idp (한국어)
description: "Configure an Amazon Cognito user pool and its users and groups and authenticate them."
content_hash: c3677f4d907b2c5fc72d321ae021ee7b30654e6d
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/aws-cognito-idp.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-cognito-idp.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aws-cognito-idp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws cognito-idp

Configure an Amazon Cognito user pool and its users and groups and authenticate them.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cognito-idp/index.html>.

- 새로운 Cognito 사용자 풀 생성:

`aws cognito-idp create-user-pool --pool-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 모든 사용자 풀 나열 :

`aws cognito-idp list-user-pools --max-results `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>

- 특정 사용자 풀 삭제:

`aws cognito-idp delete-user-pool --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_풀_아이디</span>

- 특정 풀에 사용자 생성:

`aws cognito-idp admin-create-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_풀_아이디</span>

- 특정 풀의 사용자 나열:

`aws cognito-idp list-users --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_풀_아이디</span>

- 특정 풀에서 사용자 삭제:

`aws cognito-idp admin-delete-user --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --user-pool-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_풀_아이디</span>
