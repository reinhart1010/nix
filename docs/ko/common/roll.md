---
layout: page
title: common/roll (한국어)
description: "사용자 정의 주사위 시퀀스를 굴립니다."
content_hash: d5e21d525132189ff1ec49e79c592995bcf3caeb
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/roll.html
    icon: bi bi-globe
tldri18n_status: 2
---
# roll

사용자 정의 주사위 시퀀스를 굴립니다.
더 많은 정보: <https://manned.org/roll>.

- 3개의 6면체 주사위를 굴리고 결과를 합산:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3d</span>

- 1개의 8면체 주사위를 굴리고, 3을 더하여 결과 합산:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">d8 + 3</span>

- 4개의 6면체 주사위를 굴리고 상위 3개의 결과를 유지하여 합산:

`roll `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4d6h3</span>

- 12면체 주사위 2개를 2번 굴리고 각 결과를 표시:

`roll --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2{2d12}</span>

- 2개의 20면체 주사위를 굴려 결과가 10보다 클 때까지 반복:

`roll "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2d20>10</span>`"`

- 5면체 주사위 2개를 3번 굴리고 총합을 표시:

`roll --sum-series `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3{2d5}</span>
