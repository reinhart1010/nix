---
layout: page
title: common/mat2 (한국어)
description: "다양한 파일 형식의 메타데이터를 제거하여 익명화."
content_hash: a5ecf5ae4e2eaca6f4d7b518828346ee36b03ba9
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mat2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mat2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mat2

다양한 파일 형식의 메타데이터를 제거하여 익명화.
더 많은 정보: <https://0xacab.org/jvoisin/mat2>.

- 지원되는 파일 형식 나열:

`mat2 --list`

- 파일에서 메타데이터 제거:

`mat2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 메타데이터를 제거하고 자세한 출력을 콘솔에 출력:

`mat2 --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에 있는 메타데이터를 제거하지 않고 표시:

`mat2 --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에서 메타데이터를 부분적으로 제거:

`mat2 --lightweight `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 백업을 생성하지 않고 파일에서 메타데이터를 제거:

`mat2 --inplace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
