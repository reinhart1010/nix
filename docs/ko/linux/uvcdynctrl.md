---
layout: page
title: linux/uvcdynctrl (한국어)
description: "uvcvideo에서 동적 제어를 관리하는 libwebcam 명령줄 도구."
content_hash: 60a7965680fb9638c01152d4b7be0f71dc751472
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/uvcdynctrl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# uvcdynctrl

uvcvideo에서 동적 제어를 관리하는 libwebcam 명령줄 도구.
더 많은 정보: <https://manned.org/uvcdynctrl>.

- 사용 가능한 모든 카메라 나열:

`uvcdynctrl -l`

- 특정 디바이스 사용 (`video0`이 기본값):

`uvcdynctrl -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디바이스_이름</span>

- 사용 가능한 제어 목록 나열:

`uvcdynctrl -c`

- 새로운 제어 값 설정 (음수 값을 위해서는 `-- -값` 사용):

`uvcdynctrl -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제어_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- 현재 제어 값 가져오기:

`uvcdynctrl -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">제어_이름</span>

- 현재 제어 상태를 파일에 저장:

`uvcdynctrl -W `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>

- 파일에서 제어 상태 로드:

`uvcdynctrl -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일명</span>
