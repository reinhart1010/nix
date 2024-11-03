---
layout: page
title: common/hexdump (한국어)
description: "ASCII, 10진수, 16진수, 8진수 덤프."
content_hash: 5f6b86bf50e6989c2ba926f73f80abc3783cf369
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/hexdump.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/hexdump.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/hexdump.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hexdump.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/hexdump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hexdump

ASCII, 10진수, 16진수, 8진수 덤프.
더 많은 정보: <https://manned.org/hexdump>.

- 파일의 16진수 표현을 출력하고, 중복된 줄을 '\*'로 변경:

`hexdump `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 입력 오프셋을 16진수로 표시하고 해당 ASCII 표현을 두 열로 표시:

`hexdump -C `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일의 16진수 표현을 표시하지만, 입력의 n바이트만 해석:

`hexdump -C -n`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">바이트_수</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 중복된 줄을 '\*'로 변경하지 않음:

`hexdump --no-squeezing `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
