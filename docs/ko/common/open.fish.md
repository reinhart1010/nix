---
layout: page
title: common/open.fish (한국어)
description: "파일, 디렉토리 및 URI를 기본 애플리케이션으로 엽니다."
content_hash: 6fae391bab3a2c9784a99ff5f870a2ba475ab415
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/open.fish.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/open.fish.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/open.fish.html
    icon: bi bi-globe
tldri18n_status: 2
---
# open

파일, 디렉토리 및 URI를 기본 애플리케이션으로 엽니다.
이 명령은 내장 `open` 명령이 없는 운영 체제(예: Haiku 및 macOS)에서 fish를 통해 사용할 수 있습니다.
더 많은 정보: <https://fishshell.com/docs/current/cmds/open.html>.

- 관련 애플리케이션으로 파일 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.ext</span>

- 현재 디렉토리에서 주어진 확장자를 가진 모든 파일을 관련 애플리케이션으로 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.ext</span>

- 기본 파일 관리자로 디렉토리 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 기본 웹 브라우저로 웹사이트 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 처리할 수 있는 기본 애플리케이션으로 특정 URI 열기:

`open `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tel:123</span>
