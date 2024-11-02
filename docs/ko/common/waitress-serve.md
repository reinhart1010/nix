---
layout: page
title: common/waitress-serve (한국어)
description: "순수 Python WSGI HTTP 서버."
content_hash: 06b128f48ffb6ab8b32d8d89556888b65b8e64d1
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/waitress-serve.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/waitress-serve.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># waitress-serve

순수 Python WSGI HTTP 서버.
더 많은 정보: <https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>.

- Python 웹 앱 실행:

`waitress-serve `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:wsgi_함수</span>

- localhost의 포트 8080에서 수신 대기:

`waitress-serve --listen=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:wsgi_함수</span>

- Unix 소켓에서 waitress 시작:

`waitress-serve --unix-socket=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소켓</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:wsgi_함수</span>

- 4개의 스레드를 사용하여 요청 처리:

`waitress-serve --threads=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:wsgi_함수</span>

- WSGI 객체를 반환하는 팩토리 메서드 호출:

`waitress-serve --call `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로.wsgi_팩토리</span>

- HTTPS URL 스킴 사용:

`waitress-serve --url-scheme=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:wsgi_함수</span>
