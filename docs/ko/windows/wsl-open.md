---
layout: page
title: windows/wsl-open (한국어)
description: "사용자의 기본 Windows GUI 애플리케이션에서 Windows Subsystem for Linux 내에서 파일이나 URL을 엽니다."
content_hash: 5c84c5ab584be8078ed436fc558f3b3fe2c7f4c3
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/windows/wsl-open.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/wsl-open.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wsl-open

사용자의 기본 Windows GUI 애플리케이션에서 Windows Subsystem for Linux 내에서 파일이나 URL을 엽니다.
더 많은 정보: <https://gitlab.com/4U6U57/wsl-open>.

- Windows 탐색기에서 현재 디렉토리 열기:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.</span>

- Windows에서 사용자의 기본 웹 브라우저에 URL 열기:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- Windows에서 사용자의 기본 애플리케이션에 특정 파일 열기:

`wsl-open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로\파일</span>

- `wsl-open`을 쉘의 웹 브라우저로 설정 (링크를 `wsl-open`으로 열기):

`wsl-open -w`

- 도움말 표시:

`wsl-open -h`
