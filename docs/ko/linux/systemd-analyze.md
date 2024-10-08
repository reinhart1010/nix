---
layout: page
title: linux/systemd-analyze (한국어)
description: "시스템 관리자를 분석하고 디버그하는 도구."
content_hash: 98d65c8b7997ca9bda4c34c0abef8e19afc660c5
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-analyze.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemd-analyze.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-analyze

시스템 관리자를 분석하고 디버그하는 도구.
유닛(서비스, 마운트 포인트, 장치, 소켓)의 부팅 프로세스에 대한 타이밍 세부정보를 표시.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-analyze.html>.

- 초기화에 걸린 시간 순서대로 실행 중인 모든 유닛 나열:

`systemd-analyze blame`

- 시간에 민감한 유닛 체인의 트리 출력:

`systemd-analyze critical-chain`

- 각 시스템 서비스가 시작된 시간을 보여주는 SVG 파일 생성, 초기화에 소요된 시간을 강조 표시:

`systemd-analyze plot > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.svg</span>

- 의존성 그래프를 그려 SVG 파일로 변환:

`systemd-analyze dot | dot -T`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">svg</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.svg</span>

- 실행 중인 유닛의 보안 점수 표시:

`systemd-analyze security`
