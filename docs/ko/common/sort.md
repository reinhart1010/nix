---
layout: page
title: common/sort (한국어)
description: "텍스트 파일의 줄을 정렬합니다."
content_hash: 41003fe486236c538928e28c8c5a906c938a6fc8
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sort.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/sort.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/sort.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sort.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sort

텍스트 파일의 줄을 정렬합니다.
더 많은 정보: <https://www.gnu.org/software/coreutils/sort>.

- 파일을 오름차순으로 정렬:

`sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 내림차순으로 정렬:

`sort --reverse `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 대소문자를 구분하지 않고 정렬:

`sort --ignore-case `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 알파벳 순이 아닌 숫자 순으로 정렬:

`sort --numeric-sort `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- ":"를 필드 구분자로 사용하여 3번째 필드를 기준으로 `/etc/passwd`를 숫자 순으로 정렬:

`sort --field-separator=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` --key=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- 위와 동일하지만, 3번째 필드의 항목이 동일한 경우 4번째 필드를 지수와 함께 숫자 순으로 정렬:

`sort -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3,3n</span>` -k `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4,4g</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/etc/passwd</span>

- 파일을 정렬하면서 유일한 줄만 보존:

`sort --unique `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일을 정렬하여 지정된 출력 파일에 출력 (원본 파일을 직접 정렬할 때 사용 가능):

`sort --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
