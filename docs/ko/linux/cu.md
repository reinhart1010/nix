---
layout: page
title: linux/cu (한국어)
description: "다른 시스템에 연결하여 다이얼인/직렬 터미널 역할을 하거나 오류 검사가 없는 파일 전송을 수행합니다."
content_hash: 459a4527b9377e15ea31fced9ae1c79533f5e306
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/cu.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/cu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cu

다른 시스템에 연결하여 다이얼인/직렬 터미널 역할을 하거나 오류 검사가 없는 파일 전송을 수행합니다.
더 많은 정보: <https://manned.org/cu>.

- 주어진 직렬 포트 열기:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>

- 주어진 보율로 주어진 직렬 포트 열기:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>

- 주어진 보율로 주어진 직렬 포트를 열고 문자를 로컬에서 에코(반이중 모드):

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --halfduplex`

- 주어진 보율, 패리티, 하드웨어 또는 소프트웨어 흐름 제어 없이 주어진 직렬 포트 열기:

`sudo cu --line `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyUSB0</span>` --speed `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">115200</span>` --parity=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">even|odd|none</span>` --nortscts --nostop`

- 연결 중 `cu` 세션 종료:

`~.`
