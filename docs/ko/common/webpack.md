---
layout: page
title: common/webpack (한국어)
description: "웹 프로젝트의 자바스크립트 파일과 기타 리소스를 단일 출력 파일로 묶어줍니다."
content_hash: 31cdc8b00760b27172e44e2510a4ce406d3a6179
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/webpack.html
    icon: bi bi-globe
tldri18n_status: 2
---
# webpack

웹 프로젝트의 자바스크립트 파일과 기타 리소스를 단일 출력 파일로 묶어줍니다.
더 많은 정보: <https://webpack.js.org>.

- 진입점이 되는 파일에서 단일 출력 파일 생성:

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>

- 자바스크립트 파일에서도 CSS 파일을 로드 (이 경우 `.css` 파일에 CSS 로더를 사용합니다):

`webpack `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>` --module-bind '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">css=css</span>`'`

- 구성 파일(예, 입력 스크립트 및 출력 파일 이름 포함)을 전달하고 컴파일 진행률을 표시:

`webpack --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">webpack.config.js</span>` --progress`

- 프로젝트 파일 변경 시 자동으로 다시 컴파일:

`webpack --watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">app.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bundle.js</span>
