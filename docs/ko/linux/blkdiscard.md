---
layout: page
title: linux/blkdiscard (한국어)
description: "저장 장치의 디바이스 섹터를 폐기합니다. SSD에 유용합니다."
content_hash: ada1c4885335df1995716c973c73302c1bb902dc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/blkdiscard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/blkdiscard.html
    icon: bi bi-globe
tldri18n_status: 2
---
# blkdiscard

저장 장치의 디바이스 섹터를 폐기합니다. SSD에 유용합니다.
더 많은 정보: <https://manned.org/blkdiscard>.

- 디바이스의 모든 섹터를 폐기하여 모든 데이터 제거:

`blkdiscard `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디바이스</span>

- 디바이스의 모든 블록을 안전하게 폐기하여 모든 데이터 제거:

`blkdiscard --secure `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디바이스</span>

- 디바이스의 처음 100MB를 폐기:

`blkdiscard --length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100MB</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/디바이스</span>
