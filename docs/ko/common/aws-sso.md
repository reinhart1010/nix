---
layout: page
title: common/aws-sso (한국어)
description: "SSO(Single Sign-On) 자격 증명을 사용하여 AWS 리소스에 대한 액세스를 관리."
content_hash: 5044bb9fe8081f677b8a786e5d3f53c846f7f117
last_modified_at: 2024-10-13
related_topics:
  - title: English version
    url: /en/common/aws-sso.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aws sso

SSO(Single Sign-On) 자격 증명을 사용하여 AWS 리소스에 대한 액세스를 관리.
더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sso/index.html>.

- SSO 세션을 시작하고 액세스 토큰을 새로 고침. `aws configure sso`를 사용한 설정이 필요:

`aws sso login`

- SSO 세션을 종료하고 캐시된 액세스 토큰을 지움:

`aws sso logout`

- 사용자가 액세스할 수 있는 모든 AWS 계정을 나열:

`aws sso list-accounts`

- 특정 AWS 계정에 대해 사용자가 액세스할 수 있는 모든 역할을 나열:

`aws sso list-account-roles --account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>

- 특정 계정에 대한 단기 자격 증명 검색:

`aws get-role-credentials --account-id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">계정</span>` --role-name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할</span>` --access-token `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">토큰</span>
