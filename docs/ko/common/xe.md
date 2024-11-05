---
layout: page
title: common/xe (한국어)
description: "다른 명령이나 파일에서 파이프로 전달된 각 줄에 대해 명령을 한 번 실행."
content_hash: 0e29d8cc68c5dab9ca01f6bf2d3b6d83f72e2b5b
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/xe.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xe.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xe

다른 명령이나 파일에서 파이프로 전달된 각 줄에 대해 명령을 한 번 실행.
더 많은 정보: <https://github.com/leahneukirchen/xe>.

- 입력 데이터의 각 줄을 인수로 사용하여 명령 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수_출처</span>` | xe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 명령을 실행하며, 자리 표시자(`{}`)를 입력 줄로 대체:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수_출처</span>` | xe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>` {} `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">선택적_추가_인수</span>

- 쉘스크립트를 실행하며, 매 `N`개의 줄을 하나의 호출로 결합:

`echo -e 'a\nb' | xe -N`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2</span>` -s 'echo $2 $1'`

- `.backup` 확장자를 가진 모든 파일 삭제:

`find . -name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'*.backup'</span>` | xe rm -v`

- 최대 `max-jobs` 프로세스를 병렬로 실행; 기본값은 1. `max-jobs`가 0이면 xe는 CPU 코어 수만큼 프로세스를 실행:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수_출처</span>` | xe -j `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">최대_작업</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
