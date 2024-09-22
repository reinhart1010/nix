---
layout: page
title: common/az-login (한국어)
description: "Azure에 로그인."
content_hash: 198707c21ab4432c64f748cc5db1279e315d4df1
last_modified_at: 2024-09-22
related_topics:
  - title: Deutsch version
    url: /de/common/az-login.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/az-login.html
    icon: bi bi-globe
tldri18n_status: 2
---
# az login

Azure에 로그인.
`azure-cli`의 일부 (`az`라고도 함).
더 많은 정보: <https://learn.microsoft.com/cli/azure/reference-index#az_login>.

- 대화형으로 로그인:

`az login`

- 클라이언트 암호를 사용하여 서비스 주체로 로그인:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- 클라이언트 인증서를 사용하여 서비스 주체로 로그인:

`az login --service-principal --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://azure-cli-service-principal</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/cert.pem</span>` --tenant `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">someone.onmicrosoft.com</span>

- VM의 시스템 할당 ID를 사용하여 로그인:

`az login --identity`

- VM의 사용자 할당 ID를 사용하여 로그인:

`az login --identity --username /subscriptions/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">구독_아이디</span>`/resourcegroups/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_리소스그룹</span>`/providers/Microsoft.ManagedIdentity/userAssignedIdentities/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">나의_아이디</span>
