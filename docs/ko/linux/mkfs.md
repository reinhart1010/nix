---
layout: page
title: linux/mkfs (한국어)
description: "하드 디스크 파티션에 리눅스 파일 시스템 구축."
content_hash: 458e95f5882fd19f3d053048ce917ac31b36b569
last_modified_at: 2023-10-16
related_topics:
  - title: English version
    url: /en/linux/mkfs.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/mkfs.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfs

하드 디스크 파티션에 리눅스 파일 시스템 구축.
이 명령어는 파일 시스템이 정해진 mkfs.<type>를 위해 더 이상 사용되지 않습니다.
더 많은 정보: <https://manned.org/mkfs>.

- 파티션에 Linux ext2 파일 시스템 구축:

`mkfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 지정된 타입의 파일 시스템 구축:

`mkfs -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>

- 지정된 타입의 파일 시스템을 구축하고 불량 블록을 확인:

`mkfs -c -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ntfs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파티션</span>
