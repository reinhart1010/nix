---
layout: page
title: windows/bleachbit_console (한국어)
description: "파일 시스템의 정크 파일을 정리."
content_hash: d5c6bb7251f5df71c1521ff0e113cf2f313de093
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/windows/bleachbit_console.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/windows/bleachbit_console.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bleachbit_console

파일 시스템의 정크 파일을 정리.
더 많은 정보: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Bleachbit의 그래픽 사용자 인터페이스(GUI) 버전 시작:

`bleachbit_console.exe --gui`

- 파일을 영구 삭제:

`bleachbit_console.exe --shred `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 사용 가능한 클리너 옵션 나열:

`bleachbit_console.exe --list-cleaners`

- 실제 정리 작업을 수행하기 전에 삭제될 파일과 다른 변경 사항 미리 보기:

`bleachbit_console.exe --preview `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>

- 정리 작업 수행 및 파일 삭제:

`bleachbit_console.exe --clean `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--preset|cleaner1.option1 cleaner2.* ...</span>
