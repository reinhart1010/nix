---
layout: page
title: common/wpa_supplicant (한국어)
description: "보호된 무선 네트워크 관리."
content_hash: ff21eec41b80eb28b42b4b5d890bdf61ba42a541
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wpa_supplicant.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/wpa_supplicant.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wpa_supplicant.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wpa_supplicant

보호된 무선 네트워크 관리.
더 많은 정보: <https://manned.org/wpa_supplicant.1>.

- 보호된 무선 네트워크에 연결:

`wpa_supplicant -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wpa_supplicant_conf.conf</span>

- 보호된 무선 네트워크에 연결하고 데몬으로 실행:

`wpa_supplicant -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/wpa_supplicant_conf.conf</span>
