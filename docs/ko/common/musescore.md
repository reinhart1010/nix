---
layout: page
title: common/musescore (한국어)
description: "MuseScore 3 악보 편집기."
content_hash: 36a5c3458aac7316e0b26147ea0ca14bc7798275
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/common/musescore.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/musescore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/musescore.html
    icon: bi bi-globe
tldri18n_status: 2
---
# musescore

MuseScore 3 악보 편집기.
같이 보기: `lilypond`.
더 많은 정보: <https://musescore.org/en/handbook/3/command-line-options>.

- 특정 오디오 드라이버 사용:

`musescore --audio-driver `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jack|alsa|portaudio|pulse</span>

- MP3 출력 비트레이트를 kbit/s 단위로 설정:

`musescore --bitrate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비트레이트</span>

- MuseScore를 디버그 모드로 시작:

`musescore --debug`

- 레이어와 같은 실험적 기능 활성화:

`musescore --experimental`

- 주어진 파일을 지정된 출력 파일로 내보내기. 파일 유형은 주어진 확장자에 따라 결정됨:

`musescore --export-to `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_파일</span>

- 주어진 악보 간의 차이를 출력:

`musescore --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- MIDI 가져오기 작업 파일 지정:

`musescore --midi-operations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
