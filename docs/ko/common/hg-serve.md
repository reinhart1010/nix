---
layout: page
title: common/hg-serve (한국어)
description: "리포지토리를 탐색하기 위한 독립형 Mercurial 웹 서버 시작."
content_hash: 2161d10b77f0e2bb9b0dd3c56caebadb1172978f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/hg-serve.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hg serve

리포지토리를 탐색하기 위한 독립형 Mercurial 웹 서버 시작.
더 많은 정보: <https://www.mercurial-scm.org/doc/hg.1.html#serve>.

- 웹 서버 인스턴스 시작:

`hg serve`

- 지정된 포트에서 웹 서버 인스턴스 시작:

`hg serve --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 지정된 수신 주소에서 웹 서버 인스턴스 시작:

`hg serve --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- 특정 식별자로 웹 서버 인스턴스 시작:

`hg serve --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 지정된 테마를 사용하여 웹 서버 인스턴스 시작 (템플릿 디렉토리 참조):

`hg serve --style `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스타일</span>

- 지정된 SSL 인증서 번들을 사용하여 웹 서버 인스턴스 시작:

`hg serve --certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서</span>
