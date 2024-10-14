---
layout: page
title: linux/umount (한국어)
description: "파일 시스템을 마운트 지점에서 연결 해제하여 더 이상 접근할 수 없게 만듭니다."
content_hash: 51bb2798764350c974d6bed97b22fc53d89cd07f
last_modified_at: 2024-10-14
related_topics:
  - title: English version
    url: /en/linux/umount.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/linux/umount.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/umount.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># umount

파일 시스템을 마운트 지점에서 연결 해제하여 더 이상 접근할 수 없게 만듭니다.
파일 시스템이 사용 중일 때는 마운트를 해제할 수 없습니다.
더 많은 정보: <https://manned.org/umount.8>.

- 파일 시스템을 마운트된 원본 경로를 통해 마운트 해제:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치_파일</span>

- 파일 시스템을 마운트된 대상 경로를 통해 마운트 해제:

`umount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트된_폴더</span>

- 마운트 해제가 실패할 경우, 파일 시스템을 읽기 전용으로 다시 마운트 시도:

`umount --read-only `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트된_폴더</span>

- 지정된 각 디렉토리를 재귀적으로 마운트 해제:

`umount --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/마운트된_폴더</span>

- 모든 마운트된 파일 시스템 마운트 해제 (`proc` 파일 시스템 제외):

`umount -a`
