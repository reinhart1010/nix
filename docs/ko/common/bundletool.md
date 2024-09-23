---
layout: page
title: common/bundletool (한국어)
description: "Android 애플리케이션 번들을 조작."
content_hash: 76a087dbb7c1ed20f024a168b37db68e820d2113
last_modified_at: 2024-09-23
related_topics:
  - title: English version
    url: /en/common/bundletool.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/bundletool.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># bundletool

Android 애플리케이션 번들을 조작.
`bundletool validate`와 같은 일부 하위 명0령에는 자체적인 사용법 문서가 존재.
더 많은 정보: <https://developer.android.com/tools/bundletool>.

- 하위 명령어에 대한 도움말 표시:

`bundletool help `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">하위명령어</span>

- 애플리케이션 번들에서 APK를 생성 (키 저장소 비밀번호를 묻는 메시지 표시):

`bundletool build-apks --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --ks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/key.keystore</span>` --ks-key-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.apks</span>

- 키스토어 비밀번호를 제공하는 애플리케이션 번들에서 APK를 생성:

`bundletool build-apks --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --ks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/key.keystore</span>` --ks-key-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` –ks-pass `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pass:the_password</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.apks</span>

- 보편적인 사용을 위해 단 하나의 단일 APK를 포함하는 APK 생성:

`bundletool build-apks --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --mode `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">universal</span>` --ks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/key.keystore</span>` --ks-key-alias `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">key_alias</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.apks</span>

- 에뮬레이터나 기기에 올바른 APK 조합을 설치:

`bundletool install-apks --apks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.apks</span>

- 애플리케이션의 다운로드 크기를 측정:

`bundletool get-size total --apks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.apks</span>

- 에뮬레이터 또는 장치에 대한 장치 사양 JSON 파일을 생성:

`bundletool get-device-spec --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/file.json</span>

- 번들을 확인하고 이에 대한 자세한 정보를 표시:

`bundletool validate --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>
