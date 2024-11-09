---
layout: page
title: linux/coredumpctl (한국어)
description: "저장된 코어 덤프와 메타데이터를 검색하고 처리합니다."
content_hash: 45f5f07d784b6fcb2e7d915c217b377c87e37d22
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/coredumpctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/coredumpctl.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/coredumpctl.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/coredumpctl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# coredumpctl

저장된 코어 덤프와 메타데이터를 검색하고 처리합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/coredumpctl.html>.

- 캡처된 모든 코어 덤프 나열:

`coredumpctl list`

- 특정 프로그램의 캡처된 코어 덤프 나열:

`coredumpctl list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- `PID`와 일치하는 프로그램의 코어 덤프 정보 표시:

`coredumpctl info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- 특정 프로그램의 마지막 코어 덤프를 사용하여 디버거 호출:

`coredumpctl debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>

- 특정 프로그램의 마지막 코어 덤프를 파일로 추출:

`coredumpctl --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` dump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로그램</span>
