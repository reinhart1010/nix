---
layout: page
title: common/kinit (한국어)
description: "Kerberos 서버와 주체를 인증하여 티켓을 얻고 캐시."
content_hash: 342ea1e6b1e047aee05dbe9640bccb330757cda5
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/kinit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/kinit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># kinit

Kerberos 서버와 주체를 인증하여 티켓을 얻고 캐시.
참고: Kerberos 주체는 사용자, 서비스 또는 애플리케이션일 수 있습니다.
더 많은 정보: <https://web.mit.edu/kerberos/krb5-1.12/doc/user/user_commands/kinit.html>.

- 사용자를 인증하고 티켓 발급 티켓 획득:

`kinit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 티켓 발급 티켓 갱신:

`kinit -R`

- 티켓의 유효 기간 지정:

`kinit -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5시간</span>

- 티켓의 총 갱신 가능 기간 지정:

`kinit -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1주</span>

- 다른 주체 이름으로 인증 지정:

`kinit -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주체@REALM</span>

- 다른 키탭 파일로 인증 지정:

`kinit -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/keytab</span>
