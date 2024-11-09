---
layout: page
title: linux/uncompress (한국어)
description: "Unix `compress` 명령으로 압축된 파일을 해제합니다."
content_hash: 0eefa7a839c470ea30da00882bc7180ea91c2d5e
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/uncompress.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/uncompress.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uncompress

Unix `compress` 명령으로 압축된 파일을 해제합니다.
더 많은 정보: <https://manned.org/uncompress.1>.

- 특정 파일 압축 해제:

`uncompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z 경로/대상/파일2.Z ...</span>

- 존재하지 않는 파일을 무시하고 특정 파일 압축 해제:

`uncompress -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z 경로/대상/파일2.Z ...</span>

- `stdout`에 출력 (파일은 변경되지 않고 `.Z` 파일도 생성되지 않음):

`uncompress -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z 경로/대상/파일2.Z ...</span>

- 자세히 모드 (압축 감소 또는 확장 비율을 `stderr`에 출력):

`uncompress -v `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1.Z 경로/대상/파일2.Z ...</span>
