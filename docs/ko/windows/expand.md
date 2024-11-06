---
layout: page
title: windows/expand (한국어)
description: "Windows Cabinet 파일 압축 해제."
content_hash: 7a11566689b5dab81a522e70150ff4be4ba47057
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/expand.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/expand.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/expand.html
    icon: bi bi-globe
tldri18n_status: 2
---
# expand

Windows Cabinet 파일 압축 해제.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/expand>.

- 단일 파일 Cabinet 파일을 지정한 디렉토리로 압축 해제:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>

- 소스 Cabinet 파일 내 파일 목록 표시:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` -d`

- Cabinet 파일의 모든 파일 압축 해제:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` -f:*`

- Cabinet 파일에서 특정 파일 압축 해제:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` -f:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일</span>

- 압축 해제 시 디렉토리 구조를 무시하고 단일 디렉토리에 추가:

`expand `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.cab</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\디렉토리</span>` -i`
