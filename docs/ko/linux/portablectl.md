---
layout: page
title: linux/portablectl (한국어)
description: "Linux 시스템에서 포터블 서비스 이미지를 관리하고 배포하기 위한 systemd 유틸리티."
content_hash: c90589f45c118d2a2598d735c43625fac3bc241a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/portablectl.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/portablectl.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># portablectl

Linux 시스템에서 포터블 서비스 이미지를 관리하고 배포하기 위한 systemd 유틸리티.
더 많은 정보: <https://www.freedesktop.org/software/systemd/man/portablectl.html>.

- 포터블 이미지 검색 경로에서 발견된 사용 가능한 포터블 서비스 이미지 나열:

`portablectl list`

- 호스트 시스템에 포터블 서비스 이미지 연결:

`portablectl attach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 호스트 시스템에서 포터블 서비스 이미지 연결 해제:

`portablectl detach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지|이미지_이름</span>

- 지정된 포터블 서비스 이미지의 세부 정보 및 메타데이터 표시:

`portablectl inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지</span>

- 포터블 서비스 이미지가 호스트 시스템에 연결되어 있는지 확인:

`portablectl is-attached `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/이미지|이미지_이름</span>
