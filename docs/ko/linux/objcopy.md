---
layout: page
title: linux/objcopy (한국어)
description: "오브젝트 파일의 내용을 다른 파일로 복사합니다."
content_hash: 089336a708ff65aa6252a855a44e9c673420d04f
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/objcopy.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/objcopy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/objcopy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># objcopy

오브젝트 파일의 내용을 다른 파일로 복사합니다.
더 많은 정보: <https://manned.org/objcopy>.

- 데이터를 다른 파일로 복사:

`objcopy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_파일</span>

- 오브젝트 파일을 한 형식에서 다른 형식으로 변환:

`objcopy --input-target=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">입력_형식</span>` --output-target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">출력_형식</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_파일</span>

- 파일에서 모든 심볼 정보를 제거:

`objcopy --strip-all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_파일</span>

- 파일에서 디버깅 정보 제거:

`objcopy --strip-debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_파일</span>

- 소스 파일에서 특정 섹션을 대상 파일로 복사:

`objcopy --only-section `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">섹션</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/소스_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/목표_파일</span>
