---
layout: page
title: linux/e2fsck (한국어)
description: "Linux ext2/ext3/ext4 파일 시스템을 검사합니다. 파티션은 마운트 해제되어 있어야 합니다."
content_hash: b32dbcd88dae40070acea38a2767d87a032e41d3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/e2fsck.html
    icon: bi bi-globe
tldri18n_status: 2
---
# e2fsck

Linux ext2/ext3/ext4 파일 시스템을 검사합니다. 파티션은 마운트 해제되어 있어야 합니다.
더 많은 정보: <https://manned.org/e2fsck>.

- 파일 시스템을 검사하고 손상된 블록을 보고:

`sudo e2fsck `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 파일 시스템을 검사하고 손상된 블록을 자동으로 복구:

`sudo e2fsck -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 읽기 전용 모드로 파일 시스템 검사:

`sudo e2fsck -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>

- 불량 블록을 위한 철저하고 비파괴적인 읽기-쓰기 테스트를 수행하고 블랙리스트에 추가:

`sudo e2fsck -fccky `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>
