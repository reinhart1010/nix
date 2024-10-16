---
layout: page
title: common/duf (한국어)
description: "디스크 사용량/무료 유틸리티."
content_hash: 0e9a504a546bcee82183594d4d75bf315fd73f6a
last_modified_at: 2024-10-16
related_topics:
  - title: Deutsch version
    url: /de/common/duf.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/duf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/duf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/duf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># duf

디스크 사용량/무료 유틸리티.
더 많은 정보: <https://github.com/muesli/duf>.

- 접근 가능한 장치 목록:

`duf`

- 모든 항목을 나열 (예: 의사, 중복 또는 액세스할 수 없는 파일 시스템):

`duf --all`

- 지정된 장치 또는 마운트 지점만 표시:

`duf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1 경로/대상/디렉터리2 ...</span>

- 지정된 기준에 따라 출력 결과를 정렬:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">size|used|avail|usage</span>

- 특정 파일 시스템을 표시하거나 숨김:

`duf --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">only-fs|hide-fs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tmpfs|vfat|ext4|xfs</span>

- 키별로 출력을 정렬:

`duf --sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem</span>

- 테마를 변경 (`duf`가 올바른 테마를 사용하지 못하는 경우):

`duf --theme `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">dark|light</span>
