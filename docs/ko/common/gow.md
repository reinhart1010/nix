---
layout: page
title: common/gow (한국어)
description: "Go 파일을 관찰하고 변경 사항이 있으면, 앱을 다시 시작."
content_hash: e3c1c1f05fd5177c48ec1e3ecddabe2a8df6cf5c
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/gow.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/gow.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># gow

Go 파일을 관찰하고 변경 사항이 있으면, 앱을 다시 시작.
더 많은 정보: <https://github.com/mitranim/gow>.

- 현재 디렉터리를 시작하고 감시:

`gow run .`

- 지정된 인수를 사용하여 애플리케이션을 시작:

`gow run . `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">인수1 인수2 ...</span>

- 상세 모드에서 하위 디렉터리를 보기:

`gow -v -w=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리1,경로/대상/디렉터리2,...</span>` run .`

- 지정된 파일 확장자를 확인:

`gow -e=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">go,html</span>` run .`

- 도움말 표시:

`gow -h`
