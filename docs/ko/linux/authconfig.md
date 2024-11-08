---
layout: page
title: linux/authconfig (한국어)
description: "시스템 인증 리소스를 구성합니다."
content_hash: 56e253146a82f11bc335550d4a21542a0b68e547
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/authconfig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/authconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/authconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/authconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># authconfig

시스템 인증 리소스를 구성합니다.
더 많은 정보: <https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/authconfig-install>.

- 현재 설정 표시(또는 드라이 런):

`authconfig --test`

- 서버가 다른 비밀번호 해싱 알고리즘을 사용하도록 구성:

`authconfig --update --passalgo=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">알고리즘</span>

- LDAP 인증 활성화:

`authconfig --update --enableldapauth`

- LDAP 인증 비활성화:

`authconfig --update --disableldapauth`

- 네트워크 정보 서비스 (NIS) 활성화:

`authconfig --update --enablenis`

- Kerberos 활성화:

`authconfig --update --enablekrb5`

- Winbind (액티브 디렉토리) 인증 활성화:

`authconfig --update --enablewinbindauth`

- 로컬 권한 부여 활성화:

`authconfig --update --enablelocauthorize`
