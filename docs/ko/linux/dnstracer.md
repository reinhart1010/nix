---
layout: page
title: linux/dnstracer (한국어)
description: "dnstracer 명령은 DNS가 정보를 어디서 얻는지 확인합니다."
content_hash: 2adac67d81abd96da51dde9fe169f8192a373f87
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/dnstracer.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/dnstracer.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dnstracer

dnstracer 명령은 DNS가 정보를 어디서 얻는지 확인합니다.
더 많은 정보: <https://manned.org/dnstracer>.

- 로컬 DNS가 www.example.com에 대한 정보를 어디서 얻었는지 확인:

`dnstracer `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 이미 알고 있는 특정 DNS에서 시작:

`dnstracer -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dns.example.org</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- IPv4 서버만 쿼리:

`dnstracer -4 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 실패 시 각 요청을 5번 재시도:

`dnstracer -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 실행 중 모든 단계 표시:

`dnstracer -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>

- 실행 후 수신된 모든 응답의 개요 표시:

`dnstracer -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www.example.com</span>
