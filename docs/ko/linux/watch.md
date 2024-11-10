---
layout: page
title: linux/watch (한국어)
description: "명령어를 반복 실행하고 출력 결과를 전체 화면 모드로 모니터링합니다."
content_hash: 48b4d34ea10cf7724a0bdc6c0a041192577d187a
last_modified_at: 2024-11-10
related_topics:
  - title: Deutsch version
    url: /de/linux/watch.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/watch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/watch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# watch

명령어를 반복 실행하고 출력 결과를 전체 화면 모드로 모니터링합니다.
더 많은 정보: <https://manned.org/watch>.

- 현재 디렉토리의 파일 모니터링:

`watch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ls</span>

- 디스크 공간을 모니터링하고 변경 사항 강조 표시:

`watch -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>

- "node" 프로세스를 3초마다 새로고침하며 모니터링:

`watch -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ps aux | grep node</span>`"`

- 디스크 공간을 모니터링하고 변경 시 모니터링 중지:

`watch -g `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">df</span>
