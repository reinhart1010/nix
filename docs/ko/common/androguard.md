---
layout: page
title: common/androguard (한국어)
description: "파이썬으로 작성된 안드로이드 애플리케이션 용 리버스 엔지니어링 도구입니다."
content_hash: 5591089eac7722b510e02180b49b38dbd3f7ab7b
last_modified_at: 2023-12-11
related_topics:
  - title: English version
    url: /en/common/androguard.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/androguard.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/androguard.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/androguard.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/androguard.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># androguard

파이썬으로 작성된 안드로이드 애플리케이션 용 리버스 엔지니어링 도구입니다.
더 많은 정보: <https://github.com/androguard/androguard>.

- Android 앱 매니페스트 표시:

`androguard axml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱.apk</span>

- 앱 메타데이터(버전 및 앱 아이디) 표시:

`androguard apkid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱.apk</span>

- 앱에서 자바 코드를 디컴파일:

`androguard decompile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/앱.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>
