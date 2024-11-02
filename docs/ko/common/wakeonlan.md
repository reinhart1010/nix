---
layout: page
title: common/wakeonlan (한국어)
description: "Wake-on-LAN(WOL) 기능이 활성화된 PC에 패킷 전송."
content_hash: 3375af3c5f2bd9a03ca485107d0c71438363845c
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wakeonlan.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/wakeonlan.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wakeonlan.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wakeonlan

Wake-on-LAN(WOL) 기능이 활성화된 PC에 패킷 전송.
더 많은 정보: <https://github.com/jpoliv/wakeonlan>.

- MAC 주소를 지정하여 로컬 네트워크(255.255.255.255)의 모든 장치에 패킷 전송:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- 특정 IP 주소를 통해 특정 장치로 패킷 전송:

`wakeonlan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>` -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">192.168.178.2</span>

- 명령어를 출력하지만 실행하지 않음 (드라이런):

`wakeonlan -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>

- 조용한 모드로 실행:

`wakeonlan -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">01:02:03:04:05:06</span>
