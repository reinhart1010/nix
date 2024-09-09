---
layout: page
title: common/apkleaks (한국어)
description: "APK 파일에서 URI, 엔드포인트, 비밀을 노출."
content_hash: f884e8749138d3e8db7f291c06689fa81c373420
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/common/apkleaks.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/apkleaks.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/apkleaks.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># apkleaks

APK 파일에서 URI, 엔드포인트, 비밀을 노출.
참고: APKLeaks는 `jadx` 디스어셈블러를 사용하여 APK 파일을 디컴파일.
더 많은 정보: <https://github.com/dwisiswant0/apkleaks>.

- APK 파일([f]ile)에서 URI, 엔드포인트, 비밀을 스캔:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>

- 출력([o]utput)을 스캔하여 특정 파일에 저장:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력파일.txt</span>

- `jadx` 디스어셈블러 인수([a]rguments) 전달:

`apkleaks --file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.apk</span>` --args "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">--threads-count 5 --deobf</span>`"`
