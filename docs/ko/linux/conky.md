---
layout: page
title: linux/conky (한국어)
description: "X용 경량 시스템 모니터."
content_hash: 300c61e88e7d7e7ef672459d48ee26d530124a10
last_modified_at: 2024-11-09
related_topics:
  - title: català version
    url: /ca/linux/conky.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/conky.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/conky.html
    icon: bi bi-globe
tldri18n_status: 2
---
# conky

X용 경량 시스템 모니터.
더 많은 정보: <https://github.com/brndnmtthws/conky>.

- 기본 내장 설정으로 시작:

`conky`

- 새 기본 설정 생성:

`conky -C > ~/.conkyrc`

- 지정된 설정 파일로 Conky 시작:

`conky -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정</span>

- 백그라운드에서 시작(데몬화):

`conky -d`

- 바탕화면에 Conky 정렬:

`conky -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">top|bottom|middle</span>`_`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">left|right|middle</span>

- 시작 시 5초 대기 후 실행:

`conky -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">5</span>
