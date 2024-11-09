---
layout: page
title: common/testssl (한국어)
description: "서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 확인."
content_hash: 4ca611688c935bf0212ddf12b18ddaa4e2c68816
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/testssl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/testssl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># testssl

서버에서 지원하는 SSL/TLS 프로토콜 및 암호를 확인.
더 많은 정보: <https://testssl.sh/>.

- 서버 테스트 (모든 검사를 실행) 포트 443에서:

`testssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 다른 포트 테스트:

`testssl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com:465</span>

- 사용 가능한 프로토콜만 확인:

`testssl --protocols `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 취약점만 확인:

`testssl --vulnerable `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- HTTP 보안 헤더만 확인:

`testssl --headers `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>

- 다른 STARTTLS 지원 프로토콜 테스트:

`testssl --starttls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ftp|smtp|pop3|imap|xmpp|sieve|xmpp-server|telnet|ldap|irc|lmtp|nntp|postgres|mysql</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">example.com</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>
