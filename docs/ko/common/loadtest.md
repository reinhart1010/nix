---
layout: page
title: common/loadtest (한국어)
description: "선택한 HTTP 또는 WebSockets URL에 대해 부하 테스트를 실행."
content_hash: 45cb693e640b7781b1632712e94bb6452ec7442f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/loadtest.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/loadtest.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># loadtest

선택한 HTTP 또는 WebSockets URL에 대해 부하 테스트를 실행.
더 많은 정보: <https://github.com/alexfernandez/loadtest>.

- 동시 사용자 및 초당 요청 수를 지정하여 실행:

`loadtest --concurrency `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` --rps `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">200</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 사용자 지정 HTTP 헤더와 함께 실행:

`loadtest --headers "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">accept:text/plain;text-html</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 특정 HTTP 메서드를 사용하여 실행:

`loadtest --method `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">GET</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>
