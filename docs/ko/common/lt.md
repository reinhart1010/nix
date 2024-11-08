---
layout: page
title: common/lt (한국어)
description: "Localtunnel은 로컬호스트를 외부에 노출시켜 손쉽게 테스트하고 공유할 수 있게 해줍니다."
content_hash: 4dba65770d8cb2f471a6e52834bd1e91186206a9
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/lt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# lt

Localtunnel은 로컬호스트를 외부에 노출시켜 손쉽게 테스트하고 공유할 수 있게 해줍니다.
더 많은 정보: <https://github.com/localtunnel/localtunnel>.

- 특정 포트에서 터널 시작:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>

- 포워딩을 수행하는 업스트림 서버 지정:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 특정 서브도메인 요청:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --subdomain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서브도메인</span>

- 기본 요청 정보 출력:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --print-requests`

- 기본 웹 브라우저에서 터널 URL 열기:

`lt --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8000</span>` --open`
