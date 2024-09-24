---
layout: page
title: common/bundletool-dump (한국어)
description: "Android 애플리케이션 번들을 조작."
content_hash: 1a437db01153760763072d49cabb693a03954fab
last_modified_at: 2024-09-24
related_topics:
  - title: English version
    url: /en/common/bundletool-dump.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bundletool dump

Android 애플리케이션 번들을 조작.
더 많은 정보: <https://developer.android.com/tools/bundletool>.

- 기본 모듈의 `AndroidManifest.xml`을 표시:

`bundletool dump manifest --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>

- XPath를 사용해 `AndroidManifest.xml`의 특정 값을 표시:

`bundletool dump manifest --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --xpath `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/manifest/@android:versionCode</span>

- 특정 모듈의 `AndroidManifest.xml`을 표시:

`bundletool dump manifest --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --module `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">이름</span>

- 애플리케이션 번들의 모든 리소스를 표시:

`bundletool dump resources --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>

- 특정 리소스에 대한 구성을 표시:

`bundletool dump resources --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --resource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">type/name</span>

- ID를 사용하여 특정 리소스에 대한 구성 및 값을 표시:

`bundletool dump resources --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>` --resource `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0x7f0e013a</span>` --values`

- 번들 구성 파일의 내용을 표시:

`bundletool dump config --bundle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/bundle.aab</span>
