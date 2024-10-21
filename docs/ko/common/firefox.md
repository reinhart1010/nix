---
layout: page
title: common/firefox (한국어)
description: "무료 오픈 소스 웹 브라우저."
content_hash: 2cbb15b703318e165e503ab92719c8dca72ede7d
last_modified_at: 2024-10-21
related_topics:
  - title: Deutsch version
    url: /de/common/firefox.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/firefox.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/firefox.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/firefox.html
    icon: bi bi-globe
tldri18n_status: 2
---
# firefox

무료 오픈 소스 웹 브라우저.
더 많은 정보: <https://developer.mozilla.org/en-US/docs/Mozilla/Command_Line_Options>.

- Firefox를 실행하고 웹 페이지 열기:

`firefox `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- 새로운 창 열기:

`firefox --new-window `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://www.duckduckgo.com</span>

- 비공개 (시크릿) 창을 열기:

`firefox --private-window`

- 기본 검색 엔진을 사용하여 "wikipedia"를 검색:

`firefox --search "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wikipedia</span>`"`

- 모든 확장 기능을 비활성화한 상태에서 안전 모드로 Firefox를 실행:

`firefox --safe-mode`

- 헤드리스 모드에서 웹 페이지의 스크린샷을 찍음:

`firefox --headless --screenshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.png</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- 특정 프로필을 사용하여 여러 개의 개별 Firefox 인스턴스를 동시에 실행:

`firefox --profile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉토리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com/</span>

- Firefox를 기본 브라우저로 설정:

`firefox --setDefaultBrowser`
