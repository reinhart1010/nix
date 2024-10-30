---
layout: page
title: windows/rdpsign (한국어)
description: "원격 데스크톱 프로토콜(RDP) 파일을 서명하는 도구입니다."
content_hash: 83ad1149c23be011a4c393440f716b1841f79bbd
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/windows/rdpsign.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/rdpsign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rdpsign

원격 데스크톱 프로토콜(RDP) 파일을 서명하는 도구입니다.
더 많은 정보: <https://learn.microsoft.com/windows-server/administration/windows-commands/rdpsign>.

- RDP 파일 서명:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.rdp</span>

- 특정 sha256 해시를 사용하여 RDP 파일 서명:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.rdp</span>` /sha265 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">해시</span>

- 최소 출력 설정:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.rdp</span>` /q`

- 자세한 경고, 메시지 및 상태 출력:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.rdp</span>` /v`

- 파일을 업데이트하지 않고 출력 결과를 `stdout`에 표시하여 서명을 테스트:

`rdpsign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\대상\파일.rdp</span>` /l`
