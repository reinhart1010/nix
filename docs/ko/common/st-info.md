---
layout: page
title: common/st-info (한국어)
description: "연결된 STLink 및 STM32 장치에 대한 정보를 가져옵니다."
content_hash: 13fbc35db038abb355fc8d451cc57c4ba26a8c8d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/st-info.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/st-info.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># st-info

연결된 STLink 및 STM32 장치에 대한 정보를 가져옵니다.
더 많은 정보: <https://github.com/texane/stlink>.

- 사용 가능한 프로그램 메모리 용량 표시:

`st-info --flash`

- 사용 가능한 SRAM 메모리 용량 표시:

`st-info --sram`

- 장치의 요약 정보 표시:

`st-info --probe`
