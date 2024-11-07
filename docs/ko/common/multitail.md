---
layout: page
title: common/multitail (한국어)
description: "tail의 확장판."
content_hash: 9be91d995088f1588e3d43c068eb779cba127d82
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/multitail.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/multitail.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># multitail

tail의 확장판.
더 많은 정보: <https://manned.org/multitail>.

- 패턴과 일치하는 모든 파일을 하나의 스트림에서 보여주기:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>`'`

- 디렉터리의 모든 파일을 하나의 스트림에서 보여주기:

`multitail -Q 1 '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>`/*'`

- 새 파일을 자동으로 창에 추가:

`multitail -Q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패턴</span>

- 5개의 로그 파일을 표시하고 2개를 병합하여 2개의 열에 넣되, 왼쪽 열에는 하나만 배치:

`multitail -s 2 -sn 1,3 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/병합파일</span>` -I `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일4</span>
