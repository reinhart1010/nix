---
layout: page
title: common/wiggle (한국어)
description: "`patch`가 처리할 수 없는 패치의 충돌을 해결하는 패치 적용 도구."
content_hash: 4c1e7ca53d1b8cc52e4110ead6c8bd4fa176de7b
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/wiggle.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/wiggle.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># wiggle

`patch`가 처리할 수 없는 패치의 충돌을 해결하는 패치 적용 도구.
참고: Wiggle은 모든 변경 사항을 강제로 적용하고, 충돌이 발생하면 병합하며, 해결할 수 없는 문제를 보고합니다.
더 많은 정보: <https://manned.org/wiggle>.

- 패치 파일의 변경 사항을 원본 파일에 적용:

`wiggle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/나의_패치.patch</span>

- 변경 사항을 [출력] 파일에 적용:

`wiggle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/나의_패치.patch</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일.txt</span>

- `file.rej`에서 적용되지 않은 변경 사항을 가져와서 파일에 병합:

`wiggle --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.rej</span>

- 패치 또는 병합 파일의 한 브랜치 [추출]:

`wiggle -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/나의_패치.patch</span>

- 패치를 적용하고 비교된 단어를 [출력] 파일에 저장:

`wiggle --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/나의_단어_패치.patch</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/단어_패치된_코드.c</span>

- 병합 기능에 대한 도움말 표시:

`wiggle --merge --help`
