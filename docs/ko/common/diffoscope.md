---
layout: page
title: common/diffoscope (한국어)
description: "파일, 아카이브 및 디렉터리를 비교."
content_hash: e4f7205a47e8505c3b179ce6165d7a1c6ff89b58
last_modified_at: 2024-10-12
related_topics:
  - title: English version
    url: /en/common/diffoscope.html
    icon: bi bi-globe
tldri18n_status: 2
---
# diffoscope

파일, 아카이브 및 디렉터리를 비교.
더 많은 정보: <https://diffoscope.org>.

- 2개 파일 비교:

`diffoscope `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 진행 표시줄을 보여주지 않고 두 파일을 비교:

`diffoscope --no-progress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 두 파일을 비교하고 HTML 보고서를 파일에 작성 (`stdout`에는 `-` 사용):

`diffoscope --html `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일|-</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>

- 지정된 패턴과 일치하는 이름을 가진 파일을 제외한 두 디렉터리를 비교:

`diffoscope --exclude `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리2</span>

- 두 디렉터리를 비교하고 디렉터리 메타데이터가 고려되는지 여부를 제어:

`diffoscope --exclude-directory-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">auto|yes|no|recursive</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리2</span>
