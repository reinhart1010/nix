---
layout: page
title: common/dvc-diff (한국어)
description: "DVC로 추적된 파일과 디렉토리의 변경 사항을 표시."
content_hash: 64cb94c1d83b332aa333c4cb372f5469407980b5
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/dvc-diff.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/dvc-diff.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># dvc diff

DVC로 추적된 파일과 디렉토리의 변경 사항을 표시.
더 많은 정보: <https://dvc.org/doc/command-reference/diff>.

- 다른 Git 커밋, 태그, 브랜치와 현재 작업 공간을 기준으로 DVC로 추적된 파일 비교:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋_해시/태그/브랜치</span>

- 한 Git 커밋에서 다른 커밋으로의 DVC로 추적된 파일의 변경 사항 비교:

`dvc diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">리비전2</span>

- DVC로 추적된 파일을 최신 해시와 함께 비교:

`dvc diff --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- DVC로 추적된 파일을 JSON 형식으로 출력하여 비교:

`dvc diff --show-json --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>

- DVC로 추적된 파일을 Markdown 형식으로 출력하여 비교:

`dvc diff --show-md --show-hash `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">커밋</span>
