---
layout: page
title: linux/bmon (한국어)
description: "대역폭을 모니터링하고 네트워크 관련 통계를 수집합니다."
content_hash: 7434f47a5d183cf33b92e43d4681fb2a76a33a03
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/bmon.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/bmon.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/bmon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/bmon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bmon

대역폭을 모니터링하고 네트워크 관련 통계를 수집합니다.
더 많은 정보: <https://github.com/tgraf/bmon>.

- 모든 인터페이스 목록 표시:

`bmon -a`

- 초당 비트 단위의 데이터 전송 속도 표시:

`bmon -b`

- 표시할 네트워크 인터페이스의 정책 지정:

`bmon -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인터페이스_1,인터페이스_2,인터페이스_3</span>

- 카운터당 속도를 계산하는 간격(초) 지정:

`bmon -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2.0</span>
