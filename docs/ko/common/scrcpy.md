---
layout: page
title: common/scrcpy (한국어)
description: "Android 기기를 데스크톱에서 표시하고 제어."
content_hash: 54400e3ab28653eb407515595529b0ff566bf4c0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/scrcpy.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/scrcpy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/scrcpy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># scrcpy

Android 기기를 데스크톱에서 표시하고 제어.
더 많은 정보: <https://github.com/Genymobile/scrcpy>.

- 연결된 기기의 화면 미러링:

`scrcpy`

- ID 또는 IP 주소를 기반으로 특정 기기의 화면 미러링 (`adb devices` 명령어로 확인 가능):

`scrcpy --serial `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0123456789abcdef|192.168.0.1:5555</span>

- 전체 화면 모드로 시작:

`scrcpy --fullscreen`

- 화면 회전. 각 증가 값은 반시계 방향으로 90도 회전을 추가:

`scrcpy --rotation `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0|1|2|3</span>

- 물리적 기기에서 터치 표시:

`scrcpy --show-touches`

- 화면 기록:

`scrcpy --record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp4</span>

- 드래그 앤 드롭으로 파일을 기기에 전송할 대상 디렉터리 지정 (APK가 아님):

`scrcpy --push-target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>
