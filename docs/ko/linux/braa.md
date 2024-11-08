---
layout: page
title: linux/braa (한국어)
description: "여러 호스트를 동시에 스캔할 수 있는 초고속 대량 SNMP 스캐너."
content_hash: 9fa05100f368666c5634317f8fca3148a6347965
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/braa.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/braa.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># braa

여러 호스트를 동시에 스캔할 수 있는 초고속 대량 SNMP 스캐너.
더 많은 정보: <https://github.com/mteg/braa>.

- 호스트의 SNMP 트리를 public 문자열로 탐색하여 `.1.3.6` 하위의 모든 OID 쿼리:

`braa public@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.*</span>

- `ip_range`의 전체 서브넷에 대해 `system.sysLocation.0` 쿼리:

`braa public@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip_range</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.1.2.1.1.6.0</span>

- `system.sysLocation.0`의 값을 특정 워크그룹으로 설정 시도:

`braa private@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ip</span>`:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.1.3.6.1.2.1.1.6.0</span>`=s'`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">workgroup</span>`'`
