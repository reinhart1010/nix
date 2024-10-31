---
layout: page
title: common/gnmic-subscribe (한국어)
description: "gnmic 네트워크 장치 상태 업데이트를 구독."
content_hash: f55a03750ad26ee68fa9a0a71f77666bb336461c
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gnmic-subscribe.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/gnmic-subscribe.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnmic subscribe

gnmic 네트워크 장치 상태 업데이트를 구독.
더 많은 정보: <https://gnmic.kmrd.dev/cmd/subscribe>.

- 특정 경로의 하위 트리 아래에서 대상 상태 업데이트를 구독:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>

- 샘플 간격이 30초인 대상을 구독 (기본값 10초):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --sample-interval 30s`

- 샘플 간격으로 대상을 구독하고 변경 시에만 업데이트:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --stream-mode on-change --heartbeat-interval 1m`

- 단 한 번의 업데이트만을 위해 대상을 구독:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --mode once`

- 대상을 구독하고 응답 인코딩을 지정 (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` subscribe --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --encoding json_ietf`
