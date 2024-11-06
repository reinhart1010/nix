---
layout: page
title: windows/cmstp (한국어)
description: "연결 서비스 프로필을 관리합니다."
content_hash: b908fb0ec55148e17237b97e2aad6d3b862a3c7c
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/cmstp.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/cmstp.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/cmstp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cmstp

연결 서비스 프로필을 관리합니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmstp>.

- 특정 프로필 설치:

`cmstp "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 바탕 화면 바로가기를 생성하지 않고 설치:

`cmstp /ns "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 의존성 검사를 생략하고 설치:

`cmstp /nf "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 현재 사용자만을 위해 설치:

`cmstp /su "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 모든 사용자를 위해 설치 (관리자 권한 필요):

`cmstp /au "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 프롬프트 없이 조용히 설치:

`cmstp /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 특정 프로필 제거:

`cmstp /u "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`

- 확인 프롬프트 없이 조용히 제거:

`cmstp /u /s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\프로필_파일</span>`"`
