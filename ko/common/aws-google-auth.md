---
layout: page
title: common/aws-google-auth (한국어)
description: "Google Apps를 페더레이션(Single Sign-On)공급자로 사용하여 AWS 임시(STS) 자격 증명을 획득하는 명령 줄 도구입니다."
content_hash: 59b8cf8ba7bf18993415b9d217fee9ee017b739e
related_topics:
  - title: Deutsch version
    url: /de/common/aws-google-auth.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aws-google-auth.html
    icon: bi bi-globe
---
# aws-google-auth

Google Apps를 페더레이션(Single Sign-On)공급자로 사용하여 AWS 임시(STS) 자격 증명을 획득하는 명령 줄 도구입니다.
더 많은 정보: <https://github.com/cevoaustralia/aws-google-auth>.

- IDP및 식별자를 사용하여 Google SSO에 로그인하고 자격 증명 기간을 1시간으로 설정:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- 사용자 역할을 묻는 로그인(여러 개으 사용 가능한 SAML 역할의 경우):

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a`

- AWS 계정의 별칭 확인:

`aws-google-auth -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example@example.com</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_IDP_ID</span>` -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$GOOGLE_SP_ID</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>` -a --resolve-aliases`

- 도움말 정보 보기:

`aws-google-auth -h`
