---
layout: page
title: common/mpv (한국어)
description: "MPlayer 기반의 오디오/비디오 플레이어."
content_hash: 2b57ceed24cac3e077e274a448ab6c104ebabc17
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/mpv.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/mpv.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/mpv.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/mpv.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mpv

MPlayer 기반의 오디오/비디오 플레이어.
같이 보기: `mplayer`, `vlc`.
더 많은 정보: <https://mpv.io>.

- URL 또는 파일에서 비디오나 오디오 재생:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url|경로/대상/파일</span>

- 5초 뒤로/앞으로 이동:

`LEFT <or> RIGHT`

- 1분 뒤로/앞으로 이동:

`DOWN <or> UP`

- 재생 속도를 10% 감소/증가:

`[ <or> ]`

- 현재 프레임의 스크린샷 찍기 (기본적으로 `./mpv-shotNNNN.jpg`에 저장됨):

`s`

- 지정된 속도로 파일 재생 (기본값은 1):

`mpv --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.01..100</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `mpv.conf` 파일에 정의된 프로필을 사용하여 파일 재생:

`mpv --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">프로필_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 웹캠 또는 다른 비디오 입력 장치의 출력 표시:

`mpv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/video0</span>
