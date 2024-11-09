---
layout: page
title: common/shuf (한국어)
description: "무작위 순열 생성."
content_hash: c094a441eeeb1b4536f557f434f516a0eeb80d21
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shuf.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/shuf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shuf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shuf

무작위 순열 생성.
더 많은 정보: <https://www.gnu.org/software/coreutils/shuf>.

- 파일의 줄 순서를 무작위로 섞고 결과 출력:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 결과의 처음 5개 항목만 출력:

`shuf --head-count=5 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 출력을 다른 파일에 쓰기:

`shuf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>

- 1-10 범위(포함)에서 임의의 숫자 3개 생성:

`shuf --head-count=3 --input-range=1-10 --repeat`
