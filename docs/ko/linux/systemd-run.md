---
layout: page
title: linux/systemd-run (한국어)
description: "프로그램을 일시적 범위 단위, 서비스 단위, 경로, 소켓 또는 타이머로 트리거된 서비스 단위로 실행."
content_hash: 598a68e7109cd46d16d5ccf781921b40769b7812
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-run.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/systemd-run.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-run

프로그램을 일시적 범위 단위, 서비스 단위, 경로, 소켓 또는 타이머로 트리거된 서비스 단위로 실행.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-run.html>.

- 일시적 서비스를 시작:

`sudo systemd-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 현재 사용자의 서비스 관리자에서 (권한 없이) 일시적 서비스를 시작:

`systemd-run --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 사용자 정의 단위 이름과 설명을 사용하여 일시적 서비스를 시작:

`sudo systemd-run --unit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>` --description=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 종료 후 정리되지 않는 일시적 서비스와 사용자 정의 환경 변수를 사용하여 시작:

`sudo systemd-run --remain-after-exit --set-env=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 주기적으로 일시적 서비스를 실행하는 일시적 타이머 시작 (캘린더 이벤트 형식은 `man systemd.time` 참조):

`sudo systemd-run --on-calendar=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">캘린더_이벤트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 터미널을 프로그램과 공유하여 상호작용 입력/출력을 허용하고 프로그램 종료 후 실행 세부정보를 유지:

`systemd-run --remain-after-exit --pty `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 프로세스의 속성 (예: CPUQuota, MemoryMax)을 설정하고 종료될 때까지 대기:

`systemd-run --property MemoryMax=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">메모리_바이트</span>` --property CPUQuota=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">CPU_시간_비율</span>`% --wait `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>

- 셸 파이프라인에서 프로그램 사용:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어1</span>` | systemd-run --pipe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어2</span>` | `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어3</span>
