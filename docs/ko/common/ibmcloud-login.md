---
layout: page
title: common/ibmcloud-login (한국어)
description: "IBM Cloud에 로그인하심."
content_hash: d9a4a2f48a920eebbfc895e82f9c781279eaddd4
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/ibmcloud-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ibmcloud login

IBM Cloud에 로그인하심.
더 많은 정보: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- 대화형 프롬프트를 사용하여 로그인:

`ibmcloud login`

- 특정 API 엔드포인트에 로그인 (기본값은 `cloud.ibm.com`):

`ibmcloud login -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_엔드포인트</span>

- 사용자명, 비밀번호 및 대상 지역을 매개변수로 제공하여 로그인:

`ibmcloud login -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">us-south</span>

- API 키로 로그인하고, 이를 인수로 전달:

`ibmcloud login --apikey `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">api_키_문자열</span>

- API 키로 로그인하여, 파일로 전달:

`ibmcloud login --apikey @`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/api_키_파일</span>

- 연합 ID로 로그인 (single sign-on):

`ibmcloud login --sso`
