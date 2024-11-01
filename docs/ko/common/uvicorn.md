---
layout: page
title: common/uvicorn (한국어)
description: "비동기 프로젝트를 위한 Python ASGI HTTP 서버."
content_hash: 338c96d11e6825b89a3efd5b98e369172d3efad3
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uvicorn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uvicorn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uvicorn

비동기 프로젝트를 위한 Python ASGI HTTP 서버.
더 많은 정보: <https://www.uvicorn.org/>.

- Python 웹 앱 실행:

`uvicorn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- localhost에서 포트 8080으로 수신 대기:

`uvicorn --host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:앱_객체</span>

- 라이브 리로드 활성화:

`uvicorn --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:앱_객체</span>

- 요청을 처리하기 위해 4개의 워커 프로세스 사용:

`uvicorn --workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:앱_객체</span>

- HTTPS를 통해 앱 실행:

`uvicorn --ssl-certfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.pem</span>` --ssl-keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">임포트.경로:앱_객체</span>
