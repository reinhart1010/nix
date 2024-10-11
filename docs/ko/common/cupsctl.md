---
layout: page
title: common/cupsctl (한국어)
description: "서버의 `cupsd.conf` 업데이트 또는 질의."
content_hash: 11afe53794fca1b83872a6e44ff79c5cbc0ab5e9
last_modified_at: 2024-10-11
related_topics:
  - title: English version
    url: /en/common/cupsctl.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/cupsctl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupsctl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupsctl

서버의 `cupsd.conf` 업데이트 또는 질의.
더 많은 정보: <https://openprinting.github.io/cups/doc/man-cupsctl.html>.

- 현재 구성 설정 값을 표시:

`cupsctl`

- 특정 서버의 구성 값을 표시:

`cupsctl -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">서버[:포트]</span>

- 스케줄러 연결 시 암호화를 활성화:

`cupsctl -E`

- `error_log` 파일에 대한 디버그 로깅을 활성화 또는 비활성화:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--debug-logging|--no-debug-logging</span>

- 원격 관리 활성화 또는 비활성화:

`cupsctl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--remote-admin|--no-remote-admin</span>

- 현재 디버그 로깅 상태를 구문 분석:

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`
