---
layout: page
title: linux/findmnt (한국어)
description: "파일 시스템을 찾습니다."
content_hash: 1e42a8e3125d537f88d06f8be0e469f66538b160
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/findmnt.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/findmnt.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># findmnt

파일 시스템을 찾습니다.
더 많은 정보: <https://manned.org/findmnt>.

- 모든 마운트된 파일 시스템 나열:

`findmnt`

- 디바이스 검색:

`findmnt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdb1</span>

- 마운트 지점 검색:

`findmnt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/</span>

- 특정 유형의 파일 시스템 찾기:

`findmnt -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ext4</span>

- 특정 레이블이 있는 파일 시스템 찾기:

`findmnt LABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">BigStorage</span>

- 마운트 테이블 내용을 자세히 확인하고 `/etc/fstab` 검증:

`findmnt --verify --verbose`
