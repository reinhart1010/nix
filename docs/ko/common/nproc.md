---
layout: page
title: common/nproc (한국어)
description: "사용 가능한 처리 장치 수(일반적으로 CPU)를 출력합니다."
content_hash: ea6165a35225b8591fdaa5895b359a80556aa109
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/nproc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/nproc.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/nproc.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># nproc

사용 가능한 처리 장치 수(일반적으로 CPU)를 출력합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/nproc>.

- 사용 가능한 처리 장치 수 표시:

`nproc`

- 비활성 장치를 포함한 설치된 처리 장치 수 표시:

`nproc --all`

- 가능한 경우, 반환 값에서 지정된 장치 수를 뺍니다:

`nproc --ignore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">수량</span>
