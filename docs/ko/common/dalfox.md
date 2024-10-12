---
layout: page
title: common/dalfox (한국어)
description: "자동화에 중점을 둔 강력한 오픈소스 XSS 스캐너."
content_hash: ef1149b6badfe5e87a73ee0105b2772dd62a0730
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/dalfox.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dalfox

자동화에 중점을 둔 강력한 오픈소스 XSS 스캐너.
더 많은 정보: <https://dalfox.hahwul.com/docs/usage>.

- XSS 취약점에 대한 단일 URL을 스캔:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 인증을 위해 헤더를 사용해 URL을 스캔:

`dalfox url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'X-My-Header: 123'</span>

- 파일에서 URL 목록을 스캔:

`dalfox file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
