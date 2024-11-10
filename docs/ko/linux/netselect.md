---
layout: page
title: linux/netselect (한국어)
description: "빠른 네트워크 서버 선택을 위한 속도 테스트."
content_hash: 26b0d2399c793d4e602bc7da21ac694bbc56a076
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/netselect.html
    icon: bi bi-globe
tldri18n_status: 2
---
# netselect

빠른 네트워크 서버 선택을 위한 속도 테스트.
더 많은 정보: <https://github.com/apenwarr/netselect>.

- 지연 시간이 가장 낮은 서버 선택:

`sudo netselect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_2</span>

- 네임서버 해상도 및 통계 표시:

`sudo netselect -vv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_2</span>

- 최대 TTL(수명) 정의:

`sudo netselect -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_2</span>

- 호스트 중에서 가장 빠른 N개의 서버 출력:

`sudo netselect -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">N</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트_3</span>

- 도움말 표시:

`netselect`
