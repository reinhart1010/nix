---
layout: page
title: common/whatwaf (한국어)
description: "웹 애플리케이션 방화벽 및 보호 시스템 탐지 및 우회."
content_hash: 6c988906ac7fca49145ff71773b60ee89dea02ad
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/whatwaf.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/whatwaf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/whatwaf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whatwaf

웹 애플리케이션 방화벽 및 보호 시스템 탐지 및 우회.
더 많은 정보: <https://github.com/Ekultek/WhatWaf>.

- 단일 [u]RL의 보호 시스템 탐지, 선택적으로 상세 출력 사용:

`whatwaf --url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>` --verbose`

- 파일에서 URL 목록을 병렬로 탐지 (한 줄에 하나의 URL):

`whatwaf --threads `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">숫자</span>` --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 프록시를 통해 요청을 보내고 파일에서 사용자 정의 페이로드 목록 사용 (한 줄에 하나의 페이로드):

`whatwaf --proxy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://127.0.0.1:8080</span>` --pl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 토르를 통해 요청 전송 (토르가 설치되어야 함), 사용자 정의 [p]페이로드 사용 (쉼표로 구분):

`whatwaf --tor --payloads '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">페이로드1,페이로드2,...</span>`' -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">https://example.com</span>

- 랜덤 사용자 에이전트 사용, 대역폭 조절 및 타임아웃 설정, [P]OST 요청 전송, HTTPS 연결 강제:

`whatwaf --ra --throttle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` --timeout `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>` --post --force-ssl -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>

- 탐지 가능한 모든 WAF 나열:

`whatwaf --wafs`

- 사용 가능한 모든 변조 스크립트 나열:

`whatwaf --tampers`
