---
layout: page
title: common/repren (한국어)
description: "다중 패턴 문자열 교체 및 파일 이름 바꾸기 도구."
content_hash: f5d86d8049f1cb55c27dd13154e08f2da7eb6965
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/repren.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/repren.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># repren

다중 패턴 문자열 교체 및 파일 이름 바꾸기 도구.
더 많은 정보: <https://github.com/jlevy/repren>.

- PNG 파일이 있는 디렉토리에서 리터럴 문자열 교체로 이름을 바꾸는 예비 실행:

`repren --dry-run --rename --literal --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">찾을_문자열</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">교체할_문자열</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.png</span>

- JPEG 파일이 있는 디렉토리에서 정규 표현식을 사용하여 이름을 바꾸는 예비 실행:

`repren --rename --dry-run --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">정규_표현식</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">교체할_문자열</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpg</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.jpeg</span>

- CSV 파일이 있는 디렉토리의 내용에서 찾기 및 교체 실행:

`repren --from '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">([0-9]+) 예제_문자열</span>`' --to '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">교체할_문자열 \1</span>`' `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.csv</span>

- 패턴 파일을 사용하여 찾기 및 교체와 이름 바꾸기 작업을 동시에 실행:

`repren --patterns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패턴_파일.ext</span>` --full `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>

- 대소문자를 구분하지 않고 이름 바꾸기:

`repren --rename --insensitive --patterns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/패턴_파일.ext</span>` *`
