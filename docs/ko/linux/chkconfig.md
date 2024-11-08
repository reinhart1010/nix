---
layout: page
title: linux/chkconfig (한국어)
description: "CentOS 6에서 서비스의 실행 레벨을 관리합니다."
content_hash: 8306c54bcaca516cb8d616258df1046742033478
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/chkconfig.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/chkconfig.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/chkconfig.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># chkconfig

CentOS 6에서 서비스의 실행 레벨을 관리합니다.
더 많은 정보: <https://manned.org/chkconfig>.

- 서비스와 실행 레벨 나열:

`chkconfig --list`

- 특정 서비스의 실행 레벨 표시:

`chkconfig --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>

- 부팅 시 서비스 활성화:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- 실행 레벨 2, 3, 4, 5에서 부팅 시 서비스 활성화:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2345</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sshd</span>` on`

- 부팅 시 서비스 비활성화:

`chkconfig `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`

- 실행 레벨 3에서 부팅 시 서비스 비활성화:

`chkconfig --level `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntpd</span>` off`
