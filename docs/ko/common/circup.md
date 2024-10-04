---
layout: page
title: common/circup (한국어)
description: "CircuitPython 라이브러리 업데이트 도구."
content_hash: 2527b0574f3b2f29e266eca28f4cda5eae63afff
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/circup.html
    icon: bi bi-globe
tldri18n_status: 2
---
# circup

CircuitPython 라이브러리 업데이트 도구.
더 많은 정보: <https://github.com/adafruit/circup>.

- 장치의 모듈을 대화형 방식으로 업데이트:

`circup update`

- 새로운 라이브러리 설치:

`circup install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">라이브러리_이름</span>

- 라이브러리 검색:

`circup show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">부분문자열_이름</span>

- `requirements.txt` 형식으로 연결된 장치의 모든 라이브러리를 나열:

`circup freeze`

- 연결된 장치의 모든 라이브러리를 현재 디렉터리에 저장:

`circup freeze -r`
