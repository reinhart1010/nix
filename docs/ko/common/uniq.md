---
layout: page
title: common/uniq (한국어)
description: "입력 또는 파일에서 고유한 줄을 출력합니다."
content_hash: 9f8a9e1ab8f1fb3d46b0e7a5cd26b5d90c0a94be
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/uniq.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/uniq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/uniq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># uniq

입력 또는 파일에서 고유한 줄을 출력합니다.
인접하지 않은 반복 줄을 감지하지 않으므로 먼저 정렬해야 합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/uniq>.

- 각 줄을 한 번씩만 표시:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | uniq`

- 고유한 줄만 표시:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | uniq -u`

- 중복된 줄만 표시:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | uniq -d`

- 각 줄의 발생 횟수와 함께 해당 줄 표시:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | uniq -c`

- 각 줄의 발생 횟수를 표시하고, 가장 자주 발생한 순서로 정렬:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | uniq -c | sort -nr`
