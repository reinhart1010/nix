---
layout: page
title: common/code (한국어)
description: "확장 가능한 크로스 플랫폼 코드 에디터."
content_hash: 7d278b8287a709b7cb67c84c46ac5d9aff510c15
related_topics:
  - title: Deutsch version
    url: /de/common/code.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/code.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/code.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/code.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/code.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/code.html
    icon: bi bi-globe
  - title: 中文 (繁體, 台灣) version
    url: /zh_TW/common/code.html
    icon: bi bi-globe
---
# code

확장 가능한 크로스 플랫폼 코드 에디터.
더 많은 정보: <https://github.com/microsoft/vscode>.

- Visual Studio Code 실행:

`code`

- 특정 파일 혹은 디렉토리 열기:

`code `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/혹은/디렉토리의/경로1 파일/혹은/디렉토리의/경로2 ...</span>

- 두 파일 비교:

`code --diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일의/경로1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일의/경로2</span>

- 특정 파일 혹은 디렉토리를 새로운 창에서 열기:

`code --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일/혹은/디렉토리의/경로1 파일/혹은/디렉토리의/경로2 ...</span>

- 특정 확장 프로그램 설치/삭제:

`code --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">install|uninstall</span>`-extension `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">publisher.extension</span>

- 설치된 확장 프로그램 나열:

`code --list-extensions`

- 설치된 확장 프로그램을 버전과 함께 나열:

`code --list-extensions --show-versions`

- 사용자 정보를 특정 디렉토리에 저장하면서 관리자 (루트) 권한으로 에디터 실행:

`sudo code --user-data-dir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/경로</span>
