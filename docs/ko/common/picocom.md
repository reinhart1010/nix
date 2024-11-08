---
layout: page
title: common/picocom (한국어)
description: "시리얼 콘솔을 에뮬레이트하기 위한 최소한의 프로그램."
content_hash: 5899f4329c3950e2c6e93da7921b71d85444bfad
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/picocom.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/picocom.html
    icon: bi bi-globe
tldri18n_status: 2
---
# picocom

시리얼 콘솔을 에뮬레이트하기 위한 최소한의 프로그램.
더 많은 정보: <https://manned.org/picocom>.

- 지정된 전송 속도로 시리얼 콘솔에 연결:

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --baud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">전송_속도</span>

- 특수 문자 매핑 (예: `LF`를 `CRLF`로):

`picocom `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/ttyXYZ</span>` --imap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">lfcrlf</span>
