---
layout: page
title: common/sdkmanager (한국어)
description: "Android SDK의 패키지 설치 도구."
content_hash: bea76e450e1d9b716901beef7538f5812f44bec0
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/sdkmanager.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/sdkmanager.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># sdkmanager

Android SDK의 패키지 설치 도구.
더 많은 정보: <https://developer.android.com/tools/sdkmanager>.

- 사용 가능한 패키지 나열:

`sdkmanager --list`

- 패키지 설치:

`sdkmanager `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>

- 설치된 모든 패키지 업데이트:

`sdkmanager --update`

- 패키지 제거:

`sdkmanager --uninstall `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">패키지</span>
