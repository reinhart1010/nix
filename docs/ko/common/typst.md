---
layout: page
title: common/typst (한국어)
description: "Typst 파일을 PDF로 컴파일."
content_hash: adb7657f40105ca272523c26ccdb10d434494282
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/typst.html
    icon: bi bi-globe
tldri18n_status: 2
---
# typst

Typst 파일을 PDF로 컴파일.
참고: 출력 위치 지정은 선택 사항입니다.
더 많은 정보: <https://github.com/typst/typst>.

- 주어진 디렉터리에 템플릿(예: `@preview/charged-ieee`)을 사용하여 새로운 Typst 프로젝트 초기화:

`typst init "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">템플릿</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- Typst 파일 컴파일:

`typst compile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- Typst 파일을 감시하고 변경 시 다시 컴파일:

`typst watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스.typ</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.pdf</span>

- 시스템 및 주어진 디렉토리에서 발견 가능한 모든 글꼴 나열:

`typst --font-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폰트_디렉토리</span>` fonts`
