---
layout: page
title: common/httping (한국어)
description: "웹 서버의 대기 시간과 처리량을 측정."
content_hash: 9cf3fb3a26e97e74b59f5bbabf6876e81f9a16e5
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/httping.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/httping.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># httping

웹 서버의 대기 시간과 처리량을 측정.
더 많은 정보: <https://manned.org/httping>.

- 지정된 URL을 ping:

`httping -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>

- `호스트` 및 `포트`에서 웹 서버를 ping:

`httping -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- TLS 연결을 사용하여 `호스트`에서 웹 서버를 ping:

`httping -l -g https://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- HTTP 기본 인증을 사용하여 `호스트`에서 웹 서버를 ping:

`httping -g http://`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>
