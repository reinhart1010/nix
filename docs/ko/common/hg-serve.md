---
layout: page
title: common/hg-serve (한국어)
description: "리포지토리를 탐색하기 위한 독립형 Mercurial 웹 서버 시작."
content_hash: 2161d10b77f0e2bb9b0dd3c56caebadb1172978f
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hg-serve.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/hg-serve.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hg serve

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
