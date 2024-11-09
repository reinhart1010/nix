---
layout: page
title: linux/hwinfo (한국어)
description: "시스템에 있는 하드웨어를 탐색합니다."
content_hash: 7d499833182b1642c45465a2bec13612afdcb0e6
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/hwinfo.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/hwinfo.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># hwinfo

시스템에 있는 하드웨어를 탐색합니다.
더 많은 정보: <https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>.

- 그래픽 카드 정보 가져오기:

`hwinfo --gfxcard`

- 네트워크 장치 정보 가져오기:

`hwinfo --network`

- 디스크와 CD-ROM 드라이브 목록을 출력 (출력을 줄여서 표시):

`hwinfo --short --disk --cdrom`

- 모든 하드웨어 정보를 파일에 기록:

`hwinfo --all --log `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 도움말 표시:

`hwinfo --help`
