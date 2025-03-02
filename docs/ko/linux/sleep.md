---
layout: page
title: linux/sleep (한국어)
description: "지정된 시간만큼 지연합니다."
content_hash: bcad5b999598273648fb5b946b6a0935f9091a6e
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/linux/sleep.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/sleep.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/sleep.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/sleep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sleep

지정된 시간만큼 지연합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html>.

- 초 단위로 지연:

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">초</span>

- [m]분 단위로 지연 (다른 단위로는 [d]일, [h]시간, [s]초, [inf]무한대 사용 가능):

`sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">분</span>`m`

- 1[d]일 3[h]시간 동안 지연:

`sleep 1d 3h`

- 20[m]분 지연 후 특정 명령 실행:

`sleep 20m && `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
