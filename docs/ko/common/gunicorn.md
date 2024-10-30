---
layout: page
title: common/gunicorn (한국어)
description: "Python WSGI HTTP 서버."
content_hash: c81cad8b794f1436a5196f8024efa5d815911488
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/gunicorn.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/gunicorn.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gunicorn.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gunicorn

Python WSGI HTTP 서버.
더 많은 정보: <https://gunicorn.org/>.

- Python 웹 애플리케이션 실행:

`gunicorn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- localhost의 포트 8080에서 수신 대기:

`gunicorn --bind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8080</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- 실시간 새로고침을 켜기:

`gunicorn --reload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- 요청 처리를 위해 4개의 작업자 프로세스를 사용:

`gunicorn --workers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- 요청 처리를 위해 4개의 작업자 스레드를 사용:

`gunicorn --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>

- Run app over HTTPS를 통해 애플리케이션을 실행:

`gunicorn --certfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cert.pem</span>` --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key.pem</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">import.path:app_object</span>
