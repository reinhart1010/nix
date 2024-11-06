---
layout: page
title: common/jc (한국어)
description: "여러 명령어의 출력을 JSON으로 변환."
content_hash: 437210198ee1214764dd62616b73fd412e230d47
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/jc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# jc

여러 명령어의 출력을 JSON으로 변환.
더 많은 정보: <https://github.com/kellyjonbrazil/jc>.

- 파이프를 통해 명령어 출력을 JSON으로 변환:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>

- 매직 구문을 통해 명령어 출력을 JSON으로 변환:

`jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>

- 파이프를 통해 예쁘게 출력된 JSON 출력:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>` | jc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--ifconfig</span>` -p`

- 매직 구문을 통해 예쁘게 출력된 JSON 출력:

`jc -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ifconfig</span>
