---
layout: page
title: common/streamlink (한국어)
description: "다양한 서비스에서 스트림을 추출하여 원하는 비디오 플레이어로 전달."
content_hash: 723ca78dfca2cfd70690f5d26e99d2f70cf7587b
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/streamlink.html
    icon: bi bi-globe
tldri18n_status: 2
---
# streamlink

다양한 서비스에서 스트림을 추출하여 원하는 비디오 플레이어로 전달.
더 많은 정보: <https://streamlink.github.io>.

- 지정된 URL에서 스트림을 추출하고 성공하면 선택 가능한 스트림 목록 출력:

`streamlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>

- 지정된 품질로 스트림 열기:

`streamlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">720p60</span>

- 사용할 수 있는 가장 높은 또는 낮은 품질 선택:

`streamlink `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best|worst</span>

- 특정 플레이어를 사용하여 스트림 데이터를 전달 (기본적으로 VLC가 발견되면 사용됨):

`streamlink --player=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mpv</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best</span>

- 스트림 시작 부분에서 특정 시간을 건너뜀. 라이브 스트림의 경우 스트림 끝에서부터 음수 오프셋(되감기):

`streamlink --hls-start-offset `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[HH:]MM:SS</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best</span>

- 라이브 스트림의 시작 부분으로 건너뛰거나 가능한 한 뒤로 이동:

`streamlink --hls-live-restart `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best</span>

- 스트림 데이터를 재생 대신 파일에 기록:

`streamlink --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best</span>

- 스트림을 플레이어에서 열고 동시에 파일에 기록:

`streamlink --record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ts</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com/stream</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">best</span>
