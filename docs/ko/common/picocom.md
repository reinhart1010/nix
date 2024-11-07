---
layout: page
title: common/picocom (한국어)
description: "시리얼 콘솔을 에뮬레이트하기 위한 최소한의 프로그램."
content_hash: 5899f4329c3950e2c6e93da7921b71d85444bfad
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/picocom.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/picocom.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/picocom.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># picocom

시리얼 콘솔을 에뮬레이트하기 위한 최소한의 프로그램.
더 많은 정보: <https://manned.org/picocom>.

- 지정된 전송 속도로 시리얼 콘솔에 연결:

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전송_속도</span>

- 특수 문자 매핑 (예: `LF`를 `CRLF`로):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
