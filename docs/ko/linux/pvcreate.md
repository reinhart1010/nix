---
layout: page
title: linux/pvcreate (한국어)
description: "디스크 또는 파티션을 물리적 볼륨으로 초기화합니다."
content_hash: e09b4198bc3830999bbeab4c87d32617019a5259
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/pvcreate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pvcreate

디스크 또는 파티션을 물리적 볼륨으로 초기화합니다.
같이 보기: `lvm`.
더 많은 정보: <https://manned.org/pvcreate>.

- LVM에서 사용할 수 있도록 `/dev/sda1` 볼륨 초기화:

`pvcreate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>

- 확인 프롬프트 없이 강제로 생성:

`pvcreate --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sda1</span>
