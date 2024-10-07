---
layout: page
title: linux/systemd-mount (한국어)
description: "일시적인 마운트 또는 자동 마운트 포인트를 설정하고 제거."
content_hash: b1d201a5db63648286a4240ac76a4af10fde6cc9
last_modified_at: 2024-10-07
related_topics:
  - title: English version
    url: /en/linux/systemd-mount.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/systemd-mount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/systemd-mount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># systemd-mount

일시적인 마운트 또는 자동 마운트 포인트를 설정하고 제거.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/systemd-mount.html>.

- 파일 시스템(이미지 또는 블록 장치)을 `/run/media/system/LABEL`에 마운트. LABEL은 파일 시스템 레이블이거나 레이블이 없는 경우 장치 이름:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_장치</span>

- 파일 시스템(이미지 또는 블록 장치)을 특정 위치에 마운트:

`systemd-mount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 마운트할 수 있는 파일 시스템을 가진 모든 로컬, 알려진 블록 장치 나열:

`systemd-mount --list`

- 첫 번째 접근 시 실제 파일 시스템을 마운트하는 자동 마운트 포인트 생성:

`systemd-mount --automount=yes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_장치</span>

- 하나 이상의 장치 언마운트:

`systemd-mount --umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트_또는_장치1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트_또는_장치2</span>

- 특정 파일 시스템 유형으로 파일 시스템(이미지 또는 블록 장치) 마운트:

`systemd-mount --type=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템_유형</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>

- 추가 마운트 옵션으로 파일 시스템(이미지 또는 블록 장치) 마운트:

`systemd-mount --options=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_옵션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트_포인트</span>
