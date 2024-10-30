---
layout: page
title: common/guacd (한국어)
description: "Apache Guacamole 프록시 데몬."
content_hash: 73522b25eecc14c13e9d61ab62498cda4c451f5f
last_modified_at: 2024-10-30
related_topics:
  - title: English version
    url: /en/common/guacd.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/guacd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># guacd

Apache Guacamole 프록시 데몬.
Guacamole 프로토콜과 임의의 원격 데스크톱 프로토콜(예. RDP, VNC, 기타) 간의 인터페이스를 위한 클라이언트 플러그인용 로더를 지원ㄴ.
더 많은 정보: <https://guacamole.apache.org/>.

- localhost의 특정 포트에 바인딩:

`guacd -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">127.0.0.1</span>` -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4823</span>

- 디버그 모드에서 시작하여, 프로세스를 포그라운드에 유지:

`guacd -f -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">debug</span>

- TLS 지원과 함께 시작:

`guacd -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-cert.crt</span>` -K `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">my-key.pem</span>

- PID을 파일에 작성:

`guacd -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.pid</span>
