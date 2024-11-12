---
layout: page
title: linux/semanage (한국어)
description: "SELinux 영구 정책 관리 도구."
content_hash: 0cd0d00c42769503d8abd2ab916481bd9b732ed2
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/semanage.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/semanage.html
    icon: bi bi-globe
tldri18n_status: 2
---
# semanage

SELinux 영구 정책 관리 도구.
`boolean`, `fcontext`, `port` 등의 일부 하위 명령에는 자체 사용 설명서가 있습니다.
더 많은 정보: <https://manned.org/semanage>.

- SELinux 불리언 설정 또는 해제. 불리언은 관리자가 정책 규칙이 제한된 프로세스 유형(도메인)에 어떻게 영향을 미치는지 사용자 정의할 수 있게 함:

`sudo semanage boolean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-m|--modify</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-1|--on|-0|--off</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">haproxy_connect_any</span>

- 사용자 정의 파일 컨텍스트 레이블링 규칙 추가. 파일 컨텍스트는 제한된 도메인이 접근할 수 있는 파일을 정의함:

`sudo semanage fcontext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">samba_share_t</span>` '/mnt/share(/.*)?'`

- 사용자 정의 포트 레이블링 규칙 추가. 포트 레이블은 제한된 도메인이 청취할 수 있는 포트를 정의함:

`sudo semanage port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--type</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ssh_port_t</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-p|--proto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tcp</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">22000</span>

- 제한된 도메인에 대한 허용 모드 설정 또는 해제. 도메인별 허용 모드는 `setenforce`에 비해 더 세분화된 제어를 제공함:

`sudo semanage permissive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-a|--add|-d|--delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">httpd_t</span>

- 기본 저장소에서 로컬 사용자 정의 출력:

`sudo semanage export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `semanage export`로 생성된 파일을 로컬 사용자 정의에 가져오기 (주의: 현재 사용자 정의가 제거될 수 있음!):

`sudo semanage import `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--input_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
