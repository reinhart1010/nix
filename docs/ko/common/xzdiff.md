---
layout: page
title: common/xzdiff (한국어)
description: "`xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일에 대해 `diff`를 실행."
content_hash: aad7158e02aa0bb5b39bc47c3bc742fcedd2f18e
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xzdiff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzdiff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzdiff

`xz`, `lzma`, `gzip`, `bzip2`, `lzop`, 또는 `zstd`로 압축된 파일에 대해 `diff`를 실행.
지정된 모든 옵션은 `diff`에 직접 전달됩니다.
더 많은 정보: <https://manned.org/xzdiff>.

- 두 파일 비교:

`xzdiff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 비교하여 차이를 나란히 표시:

`xzdiff --side-by-side `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 비교하고 다르다는 것만 보고(차이점 세부사항은 없음):

`xzdiff --brief `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 비교하고 파일이 동일할 때 보고:

`xzdiff --report-identical-files `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 페이지 단위로 결과를 보여주며 두 파일 비교:

`xzdiff --paginate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>
