---
layout: page
title: linux/rc-service (한국어)
description: "매개변수를 사용하여 OpenRC 서비스를 찾아 실행합니다."
content_hash: 3012cb72f7bd24212191911fb0df75258f95029a
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/rc-service.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rc-service

매개변수를 사용하여 OpenRC 서비스를 찾아 실행합니다.
같이 보기: `openrc`.
더 많은 정보: <https://manned.org/rc-service>.

- 서비스 상태 표시:

`rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` status`

- 서비스 시작:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` start`

- 서비스 중지:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` stop`

- 서비스 재시작:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` restart`

- 서비스의 사용자 지정 명령을 실행 시뮬레이션:

`sudo rc-service --dry-run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_이름</span>

- 서비스의 사용자 지정 명령 실제 실행:

`sudo rc-service `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령_이름</span>

- 디스크에서 서비스 정의 위치 확인:

`sudo rc-service --resolve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서비스_이름</span>
