---
layout: page
title: common/nodemon (한국어)
description: "파일을 감시하고 변경 사항이 감지되면 Node 애플리케이션을 자동으로 재시작."
content_hash: 6003cf94f248482bcafef9ea51f78c5644a30b25
last_modified_at: 2024-11-06
related_topics:
  - title: Deutsch version
    url: /de/common/nodemon.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/nodemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# nodemon

파일을 감시하고 변경 사항이 감지되면 Node 애플리케이션을 자동으로 재시작.
더 많은 정보: <https://nodemon.io>.

- 지정된 파일을 실행하고 특정 파일의 변경 사항 감시:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 수동으로 nodemon 재시작(이 기능을 사용하려면 nodemon이 이미 활성 상태여야 함):

`rs`

- 특정 파일 무시:

`nodemon --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_폴더</span>

- Node 애플리케이션에 인수 전달:

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들</span>

- nodemon 인수가 아닌 경우 Node 자체에 인수 전달(예: `--inspect`):

`nodemon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수들</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.js</span>

- 임의의 비-Node 스크립트 실행:

`nodemon --exec "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스크립트를_실행할_명령</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션들</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트</span>

- Python 스크립트 실행:

`nodemon --exec "python `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션들</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.py</span>
