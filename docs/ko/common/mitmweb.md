---
layout: page
title: common/mitmweb (한국어)
description: "웹 기반의 대화형 중간자(MITM) HTTP 프록시."
content_hash: 9f8452df016b3051c1cbd11a67c7871c70b5286f
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mitmweb.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mitmweb.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mitmweb

웹 기반의 대화형 중간자(MITM) HTTP 프록시.
같이 보기: `mitmproxy`.
더 많은 정보: <https://docs.mitmproxy.org/stable/concepts-options>.

- 기본 설정으로 `mitmweb` 시작:

`mitmweb`

- 사용자 지정 주소와 포트로 `mitmweb` 시작:

`mitmweb --listen-host `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">IP_주소</span>` --listen-port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- 트래픽을 처리하기 위해 스크립트를 사용하여 `mitmweb` 시작:

`mitmweb --scripts `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/스크립트.py</span>
