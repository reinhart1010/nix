---
layout: page
title: common/avrdude (한국어)
description: "Atmel AVR 마이크로 컨트롤러 프로그래밍을 위한 드라이버 프로그램."
content_hash: 9ebfa6f710368fc3e31ae083dfa77a6bccc2d599
related_topics:
  - title: Deutsch version
    url: /de/common/avrdude.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/avrdude.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/avrdude.html
    icon: bi bi-globe
---
# avrdude

Atmel AVR 마이크로 컨트롤러 프로그래밍을 위한 드라이버 프로그램.
더 많은 정보: <https://www.nongnu.org/avrdude/>.

- AVR 마이크로 컨트롤러 읽기:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AVR_device</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` -U flash:r:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>`:i`

- AVR 마이크로 컨트롤러 쓰기:

`avrdude -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">AVR_device</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programmer</span>` -U flash:w:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">file.hex</span>

- 사용 가능한 AVR 장치 목록:

`avrdude -p \?`

- 사용 가능한 AVR 프로그래머 목록:

`avrdude -c \?`
