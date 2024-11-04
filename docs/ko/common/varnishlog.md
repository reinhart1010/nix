---
layout: page
title: common/varnishlog (한국어)
description: "Varnish 로그 표시."
content_hash: 0a69fa6259050dd949c068d49e5a3b193a3d4ae9
last_modified_at: 2024-11-04
related_topics:
  - title: English version
    url: /en/common/varnishlog.html
    icon: bi bi-globe
tldri18n_status: 2
---
# varnishlog

Varnish 로그 표시.
더 많은 정보: <https://varnish-cache.org/docs/trunk/reference/varnishlog.html>.

- 실시간으로 로그 표시:

`varnishlog`

- 특정 도메인에 대한 요청만 표시:

`varnishlog -q 'ReqHeader eq "Host: `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`"'`

- POST 요청만 표시:

`varnishlog -q 'ReqMethod eq "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">POST</span>`"'`

- 특정 경로에 대한 요청만 표시:

`varnishlog -q 'ReqURL eq "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/경로</span>`"'`

- 정규 표현식과 일치하는 경로에 대한 요청만 표시:

`varnishlog -q 'ReqURL ~ "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규표현식</span>`"'`
