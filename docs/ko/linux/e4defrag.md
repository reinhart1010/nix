---
layout: page
title: linux/e4defrag (한국어)
description: "ext4 파일 시스템을 조각 모음합니다."
content_hash: 69d072179f977039a9e36a9dba28570a5a09233f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/e4defrag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# e4defrag

ext4 파일 시스템을 조각 모음합니다.
더 많은 정보: <https://manned.org/e4defrag>.

- 파일 시스템 조각 모음:

`e4defrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템이 얼마나 조각화되었는지 확인:

`e4defrag -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 오류와 각 파일의 조각화 개수를 조각 모음 전후에 출력:

`e4defrag -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
