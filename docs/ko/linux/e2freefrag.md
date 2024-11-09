---
layout: page
title: linux/e2freefrag (한국어)
description: "ext2/ext3/ext4 파일시스템의 여유 공간 조각화 정보를 출력합니다."
content_hash: f6c0c0b512ec5aa3dde609fcda0caf24acedf8cc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/e2freefrag.html
    icon: bi bi-globe
tldri18n_status: 2
---
# e2freefrag

ext2/ext3/ext4 파일시스템의 여유 공간 조각화 정보를 출력합니다.
더 많은 정보: <https://manned.org/e2freefrag>.

- 연속적이고 정렬된 여유 공간으로 존재하는 여유 블록 수 확인:

`e2freefrag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 청크 크기를 킬로바이트 단위로 지정하여 사용 가능한 여유 청크 수 출력:

`e2freefrag -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">청크_크기_kb</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
