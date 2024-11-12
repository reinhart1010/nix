---
layout: page
title: osx/screencapture (한국어)
description: "스크린샷과 화면 녹화를 위한 유틸리티."
content_hash: 462fbbe7080743c43f3e7ab82c55d31e6d7876a1
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/osx/screencapture.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/osx/screencapture.html
    icon: bi bi-globe
tldri18n_status: 2
---
# screencapture

스크린샷과 화면 녹화를 위한 유틸리티.
더 많은 정보: <https://keith.github.io/xcode-man-pages/screencapture.1.html>.

- 스크린샷을 찍어 파일로 저장:

`screencapture `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 마우스 커서를 포함하여 스크린샷 찍기:

`screencapture -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 스크린샷을 찍고 저장하는 대신 미리보기로 열기:

`screencapture -P`

- 선택한 직사각형 영역의 스크린샷 찍기:

`screencapture -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 지연 후 스크린샷 찍기:

`screencapture -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.png</span>

- 화면 녹화를 하고 파일로 저장:

`screencapture -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.mp4</span>
