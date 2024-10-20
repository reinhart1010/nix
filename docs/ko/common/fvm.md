---
layout: page
title: common/fvm (한국어)
description: "Flutter 버전 관리."
content_hash: eb016a77ff36e184b4fa0279e3aa63d33521cfef
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/fvm.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/fvm.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fvm.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fvm

Flutter 버전 관리.
더 많은 정보: <https://fvm.app/documentation/guides/basic-commands>.

- Flutter SDK 버전을 설치. 프로젝트 설정에 `version` 없이 사용:

`fvm install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- 프로젝트에서 특정 버전의 Flutter SDK를 설치:

`fvm use `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">옵션</span>

- Flutter SDK의 글로벌 버전을 설정:

`fvm global `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- FVM 캐시 삭제:

`fvm destroy`

- Flutter SDK의 특정 버전을 제거:

`fvm remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- Flutter SDK의 설치된 모든 버전을 나열:

`fvm list`

- Flutter SDK의 모든 릴리스를 나열:

`fvm releases`
