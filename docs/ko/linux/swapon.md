---
layout: page
title: linux/swapon (한국어)
description: "디바이스와 파일을 스왑에 사용할 수 있도록 활성화합니다."
content_hash: 328c8aec9ec81fcc5bfed46e6adc74affe8cbcee
last_modified_at: 2024-11-11
related_topics:
  - title: English version
    url: /en/linux/swapon.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/swapon.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># swapon

디바이스와 파일을 스왑에 사용할 수 있도록 활성화합니다.
참고: `경로/대상/파일`은 일반 파일이나 스왑 파티션을 가리킬 수 있습니다.
더 많은 정보: <https://manned.org/swapon>.

- 스왑 정보를 표시:

`swapon`

- 주어진 스왑 영역 활성화:

`swapon `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `/etc/fstab`에 지정된 모든 스왑 영역(단, `noauto` 옵션이 있는 것은 제외) 활성화:

`swapon --all`

- 레이블로 스왑 파티션 활성화:

`swapon -L `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>
