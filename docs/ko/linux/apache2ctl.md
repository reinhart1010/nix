---
layout: page
title: linux/apache2ctl (한국어)
description: "Apache HTTP 웹 서버 관리."
content_hash: fe3506afe3973916838b0e0e04261358c42d04f4
last_modified_at: 2024-11-08
related_topics:
  - title: Deutsch version
    url: /de/linux/apache2ctl.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apache2ctl.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apache2ctl.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apache2ctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apache2ctl.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apache2ctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/apache2ctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apache2ctl

Apache HTTP 웹 서버 관리.
이 명령은 Debian 기반 OS에 포함되어 있으며, RHEL 기반 OS에서는 `httpd`를 참조하세요.
더 많은 정보: <https://manned.org/apache2ctl.8>.

- Apache 데몬 시작. 이미 실행 중인 경우 메시지 표시:

`sudo apache2ctl start`

- Apache 데몬 중지:

`sudo apache2ctl stop`

- Apache 데몬 재시작:

`sudo apache2ctl restart`

- 구성 파일의 구문 테스트:

`sudo apache2ctl -t`

- 로드된 모듈 나열:

`sudo apache2ctl -M`
