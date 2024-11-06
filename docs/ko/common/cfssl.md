---
layout: page
title: common/cfssl (한국어)
description: "Cloudflare의 PKI 및 TLS 툴킷."
content_hash: 1206326eb5a2c06e24c60605ce479c17dddc5a22
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/cfssl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cfssl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cfssl

Cloudflare의 PKI 및 TLS 툴킷.
참고: `openssl`.
더 많은 정보: <https://github.com/cloudflare/cfssl>.

- 호스트의 인증서 정보 표시:

`cfssl certinfo -domain `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.google.com</span>

- 파일에서 인증서 정보를 디코딩:

`cfssl certinfo -cert `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/인증서.pem</span>

- 호스트에서 SSL/TLS 문제를 검색:

`cfssl scan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트1 호스트2 ...</span>

- 하위 명령에 대한 도움말 표시:

`cfssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">genkey|gencsr|certinfo|sign|gencrl|ocspdump|ocsprefresh|ocspsign|ocspserve|scan|bundle|crl|print-defaults|revoke|gencert|serve|version|selfsign|info</span>` -h`
