---
layout: page
title: common/ifconfig (한국어)
description: "네트워크 인터페이스 구성자."
content_hash: 603e3bccdc860ce431f57a63b5c72eedddeebcc0
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/ifconfig.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/ifconfig.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ifconfig.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/ifconfig.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ifconfig.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ifconfig

네트워크 인터페이스 구성자.
더 많은 정보: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- 인터페이스 네트워크 설정 보기:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>

- 비활성화된 인터페이스를 포함하여, 모든 인터페이스의 세부 정보를 표시:

`ifconfig -a`

- 인터페이스 비활성화:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` down`

- 인터페이스 활성화:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` up`

- 인터페이스에 IP 주소를 할당:

`ifconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_주소</span>
