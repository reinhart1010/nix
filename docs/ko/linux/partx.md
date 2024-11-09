---
layout: page
title: linux/partx (한국어)
description: "파티션 테이블을 해석하고 커널에 정보를 전달합니다."
content_hash: 1096b39ce55cc374f09a1571a63d92e0248aacd3
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/partx.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/partx.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># partx

파티션 테이블을 해석하고 커널에 정보를 전달합니다.
더 많은 정보: <https://manned.org/partx>.

- 블록 디바이스 또는 디스크 이미지의 파티션 나열:

`sudo partx --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디바이스_또는_디스크_이미지</span>

- 주어진 블록 디바이스에서 찾은 모든 파티션을 커널에 추가:

`sudo partx --add --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디바이스_또는_디스크_이미지</span>

- 커널에서 모든 파티션 삭제(디스크의 파티션은 변경하지 않음):

`sudo partx --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디바이스_또는_디스크_이미지</span>
