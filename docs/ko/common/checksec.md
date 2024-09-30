---
layout: page
title: common/checksec (한국어)
description: "실행 파일의 보안 속성을 확인."
content_hash: 335448379109e157fc3704c32c79e3c8457453a3
last_modified_at: 2024-09-30
related_topics:
  - title: English version
    url: /en/common/checksec.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/checksec.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># checksec

실행 파일의 보안 속성을 확인.
더 많은 정보: <https://github.com/slimm609/checksec.sh>.

- 실행 가능한 바이너리 파일의 보안 속성을 확인:

`checksec --file=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/바이너리</span>

- 디렉터리에 있는 모든 실행 파일의 보안 속성을 반복적으로 나열:

`checksec --dir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 프로세스의 보안 속성을 나열:

`checksec --proc=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- 실행 중인 커널의 보안 속성을 나열:

`checksec --kernel`
