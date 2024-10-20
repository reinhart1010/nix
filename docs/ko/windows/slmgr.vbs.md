---
layout: page
title: windows/slmgr.vbs (한국어)
description: "Windows 라이선스를 설치, 활성화 및 관리합니다."
content_hash: a908eda1b03118dbcd5dd5de3b7bad375629d19b
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/slmgr.vbs.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/slmgr.vbs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# slmgr.vbs

Windows 라이선스를 설치, 활성화 및 관리합니다.
이 명령어는 현재 Windows 라이선스를 덮어쓰거나 비활성화하거나 제거할 수 있습니다. 주의하여 사용하세요.
더 많은 정보: <https://learn.microsoft.com/windows-server/get-started/activation-slmgr-vbs-options>.

- 현재 Windows 라이선스 정보 표시:

`slmgr.vbs /dli`

- 현재 장치의 설치 ID 표시. 오프라인 라이선스 활성화에 유용합니다:

`slmgr.vbs /dti`

- 현재 라이선스의 만료 날짜 및 시간 표시:

`slmgr.vbs /xpr`

- 새로운 Windows 라이선스 제품 키 설치. 관리자 권한이 필요하며 기존 라이선스를 덮어씁니다:

`slmgr.vbs /ipk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제품_키</span>

- Windows 제품 라이선스 온라인 활성화. 관리자 권한이 필요합니다:

`slmgr.vbs /ato`

- Windows 제품 라이선스 오프라인 활성화. 관리자 권한이 필요하며 Microsoft Product Activation Center에서 제공하는 확인 아이디가 필요합니다:

`slmgr.vbs /atp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">확인_아이디</span>

- 현재 라이선스의 제품 키를 Windows 레지스트리에서 제거합니다. 이는 현재 라이선스를 비활성화하거나 제거하지 않으며 키가 악성 프로그램에 의해 도난당하는 것을 방지합니다:

`slmgr.vbs /cpky`

- 현재 라이선스 제품 키 제거:

`slmgr.vbs /upk`
