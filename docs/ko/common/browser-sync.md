---
layout: page
title: common/browser-sync (한국어)
description: "파일 변경에 따라 브라우저를 업데이트 하는 로컬 웹 서버 시작."
content_hash: 74740e2f7349d9b07fa3badf0fadb71b06bfcb1b
last_modified_at: 2024-03-14
related_topics:
  - title: English version
    url: /en/common/browser-sync.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/browser-sync.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/browser-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# browser-sync

파일 변경에 따라 브라우저를 업데이트 하는 로컬 웹 서버 시작.
더 많은 정보: <https://browsersync.io/docs/command-line>.

- 특정 디렉토리로부터 서버 시작:

`browser-sync start --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>` --files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>

- 로컬 디렉토리에서 서버 시작, 일부 디렉토리에서 모든 CSS파일 확인:

`browser-sync start --server --files '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로/*.css</span>`'`

- 구성 파일 생성:

`browser-sync init`

- 구성 파일에서 브라우저 동기화 시작:

`browser-sync start --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">config_파일</span>
