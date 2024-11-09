---
layout: page
title: common/stripe (한국어)
description: "Stripe 계정과 상호 작용."
content_hash: f896d33afa5bd1831aaaecc68f919a9c1a9d3f8d
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/stripe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/stripe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># stripe

Stripe 계정과 상호 작용.
더 많은 정보: <https://docs.stripe.com/stripe-cli>.

- 계정 활동 로그 팔로우:

`stripe logs tail`

- `charge.succeeded` 이름의 이벤트를 필터링하여 이벤트 수신 대기하고 이를 localhost:3000/events로 전달:

`stripe listen --events="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charge.succeeded</span>`" --forward-to="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">localhost:3000/events</span>`"`

- 테스트 웹훅 이벤트 전송:

`stripe trigger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">charge.succeeded</span>

- 고객 생성:

`stripe customers create --email="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">테스트@example.com</span>`" --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Jenny Rosen</span>`"`

- JSON으로 출력:

`stripe listen --print-json`
