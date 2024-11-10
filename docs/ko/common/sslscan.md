---
layout: page
title: common/sslscan (한국어)
description: "서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 검사."
content_hash: 0681d74ce1cc1f7b32914226cd9fa1202b440df4
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/sslscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sslscan

서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 검사.
더 많은 정보: <https://github.com/rbsec/sslscan>.

- 포트 443에서 서버 테스트:

`sslscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 지정된 포트에서 테스트:

`sslscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">465</span>

- 인증서 정보 표시:

`testssl --show-certificate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>
