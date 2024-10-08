---
layout: page
title: linux/systemd-sysext (한국어)
description: "시스템 확장 이미지를 활성화하거나 비활성화합니다."
content_hash: 17ad731c217e1522de18365fe76ace8a854362b7
last_modified_at: 2024-10-08
related_topics:
  - title: English version
    url: /en/linux/systemd-sysext.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/systemd-sysext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# systemd-sysext

시스템 확장 이미지를 활성화하거나 비활성화합니다.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-sysext.html>.

- 설치된 확장 이미지 나열:

`systemd-sysext list`

- 시스템 확장 이미지를 `/usr/` 및 `/opt/`에 병합:

`systemd-sysext merge`

- 현재 병합 상태 확인:

`systemd-sysext status`

- 현재 설치된 모든 시스템 확장 이미지를 `/usr/` 및 `/opt/`에서 제거:

`systemd-sysext unmerge`

- 시스템 확장 이미지 새로 고침 (`unmerge` 및 `merge`의 조합):

`systemd-sysext refresh`
