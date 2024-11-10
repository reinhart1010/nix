---
layout: page
title: linux/mocp (한국어)
description: "Music on Console (MOC) 오디오 플레이어."
content_hash: 2118d1ff8380b3f584f46671425ac9d4955b6490
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/mocp.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mocp

Music on Console (MOC) 오디오 플레이어.
더 많은 정보: <https://manned.org/mocp>.

- MOC 터미널 UI 실행:

`mocp`

- 특정 디렉토리에서 MOC 터미널 UI 실행:

`mocp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- MOC 터미널 UI를 실행하지 않고 백그라운드에서 MOC 서버 시작:

`mocp --server`

- MOC가 백그라운드에서 실행 중일 때 특정 곡을 재생 목록에 추가:

`mocp --enqueue `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오_파일</span>

- MOC가 백그라운드에서 실행 중일 때 재귀적으로 곡을 재생 목록에 추가:

`mocp --append `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- MOC가 백그라운드에서 실행 중일 때 재생 목록 지우기:

`mocp --clear`

- MOC가 백그라운드에서 실행 중일 때 현재 대기 중인 곡 재생 또는 정지:

`mocp --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">play|stop</span>

- MOC 서버를 백그라운드에서 중지:

`mocp --exit`
