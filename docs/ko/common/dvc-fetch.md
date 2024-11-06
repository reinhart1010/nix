---
layout: page
title: common/dvc-fetch (한국어)
description: "원격 저장소에서 DVC로 추적된 파일 및 디렉토리를 다운로드."
content_hash: c337619b69e7d8942876cae216c5f1b48c971f97
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/dvc-fetch.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dvc-fetch.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dvc fetch

원격 저장소에서 DVC로 추적된 파일 및 디렉토리를 다운로드.
더 많은 정보: <https://dvc.org/doc/command-reference/fetch>.

- 기본 원격 업스트림 저장소(설정된 경우)에서 최신 변경사항 가져오기:

`dvc fetch`

- 특정 원격 업스트림 저장소에서 변경사항 가져오기:

`dvc fetch --remote `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원격_이름</span>

- 특정 대상의 최신 변경사항 가져오기:

`dvc fetch `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상/들</span>

- 모든 브랜치 및 태그의 변경사항 가져오기:

`dvc fetch --all-branches --all-tags`

- 모든 커밋의 변경사항 가져오기:

`dvc fetch --all-commits`
