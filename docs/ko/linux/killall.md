---
layout: page
title: linux/killall (한국어)
description: "프로세스 이름으로 모든 인스턴스에 종료 신호를 보냅니다 (정확한 이름이어야 함)."
content_hash: 21323f1fbbf6616deacc148ba5e0622808440b73
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/killall.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/killall.html
    icon: bi bi-globe
tldri18n_status: 2
---
# killall

프로세스 이름으로 모든 인스턴스에 종료 신호를 보냅니다 (정확한 이름이어야 함).
SIGKILL 및 SIGSTOP을 제외한 모든 신호는 프로세스에서 가로챌 수 있어 깨끗한 종료가 가능합니다.
더 많은 정보: <https://manned.org/killall>.

- 기본 SIGTERM(종료) 신호를 사용하여 프로세스 종료:

`killall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 사용 가능한 신호 이름 나열('SIG' 접두사 없이 사용):

`killall --list`

- 종료 전에 확인을 요청:

`killall -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- SIGINT(인터럽트) 신호를 사용하여 프로세스 종료, 이는 `Ctrl + C`를 눌렀을 때 보내지는 신호와 동일:

`killall -INT `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>

- 프로세스를 강제로 종료:

`killall -KILL `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로세스_이름</span>
