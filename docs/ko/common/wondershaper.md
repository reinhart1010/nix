---
layout: page
title: common/wondershaper (한국어)
description: "네트워크 어댑터의 대역폭을 제한할 수 있도록 합니다."
content_hash: fa044c73ca7f4b88fba7d3aefb52f9f98f30b97b
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/wondershaper.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wondershaper

네트워크 어댑터의 대역폭을 제한할 수 있도록 합니다.
더 많은 정보: <https://github.com/magnific0/wondershaper#usage>.

- [h]elp 표시:

`wondershaper -h`

- 특정 [a]dapter의 현재 [s]tatus 보기:

`wondershaper -s -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터_이름</span>

- 특정 [a]dapter의 제한 해제:

`wondershaper -c -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터_이름</span>

- 특정 최대 [d]ownload 속도 설정 (Kbps 단위):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터_이름</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>

- 특정 최대 [u]pload 속도 설정 (Kbps 단위):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터_이름</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>

- 특정 최대 [d]ownload 및 [u]pload 속도 설정 (Kbps 단위):

`wondershaper -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">어댑터_이름</span>` -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1024</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">512</span>
