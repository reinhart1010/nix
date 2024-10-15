---
layout: page
title: linux/mkfs.fat (한국어)
description: "파티션 내에 MS-DOS 파일 시스템 생성."
content_hash: 23ed0d588e5095cc5aa21638592d11001f928d9a
last_modified_at: 2024-10-15
related_topics:
  - title: English version
    url: /en/linux/mkfs.fat.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/mkfs.fat.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/mkfs.fat.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfs.fat

파티션 내에 MS-DOS 파일 시스템 생성.
더 많은 정보: <https://manned.org/mkfs.fat>.

- 장치 b의 파티션 1 (`sdb1`) 에 fat 파일 시스템 생성:

`mkfs.fat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 이름을 지정하여 파일 시스템 생성:

`mkfs.fat -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 볼륨 ID를 지정하여 파일 시스템 생성:

`mkfs.fat -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">볼륨_ID</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 파일 할당 테이블을 2개 대신 5개 사용:

`mkfs.fat -f 5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>
