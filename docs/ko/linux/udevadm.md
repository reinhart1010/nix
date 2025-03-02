---
layout: page
title: linux/udevadm (한국어)
description: "Linux `udev` 관리 도구."
content_hash: 689fc153ba3d3da876dd2c7d1b76b14cbe902fcb
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/udevadm.html
    icon: bi bi-globe
tldri18n_status: 2
---
# udevadm

Linux `udev` 관리 도구.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/udevadm>.

- 모든 장치 이벤트 모니터링:

`sudo udevadm monitor`

- 커널에 의해 전송된 `uevent` 출력:

`sudo udevadm monitor --kernel`

- `udev`에 의해 처리된 후의 장치 이벤트 출력:

`sudo udevadm monitor --udev`

- 장치 `/dev/sda`의 속성 나열:

`sudo udevadm info --attribute-walk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>

- 모든 `udev` 규칙 다시 로드:

`sudo udevadm control --reload`

- 모든 `udev` 규칙 실행 트리거:

`sudo udevadm trigger`

- `/dev/sda` 로딩을 시뮬레이션하여 이벤트 실행 테스트:

`sudo udevadm test `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda</span>
