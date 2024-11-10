---
layout: page
title: linux/resize2fs (한국어)
description: "ext2, ext3 또는 ext4 파일 시스템 크기 조정."
content_hash: 5eb0359afcd7ffe2dff498459dc3f5f61d8911a0
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/resize2fs.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/resize2fs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# resize2fs

ext2, ext3 또는 ext4 파일 시스템 크기 조정.
기본 파티션 크기를 조정하지 않습니다. 파일 시스템을 먼저 마운트 해제해야 할 수도 있으며, 자세한 내용은 man 페이지를 참조하세요.
더 많은 정보: <https://manned.org/resize2fs>.

- 파일 시스템을 자동으로 크기 조정:

`resize2fs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 진행 표시줄을 표시하며 파일 시스템을 40G 크기로 조정:

`resize2fs -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">40G</span>

- 파일 시스템을 가능한 최소 크기로 축소:

`resize2fs -M `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
