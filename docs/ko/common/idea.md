---
layout: page
title: common/idea (한국어)
description: "JetBrains Java 및 Kotlin IDE."
content_hash: 0995c3828c5a2c8fffb819834772d8962b370c03
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/idea.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/idea.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># idea

JetBrains Java 및 Kotlin IDE.
더 많은 정보: <https://www.jetbrains.com/help/idea/working-with-the-ide-features-from-command-line.html>.

- IntelliJ IDEA에서 현재 디렉터리를 열기:

`idea `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- IntelliJ IDEA에서 특정 파일이나 디렉터리를 열기:

`idea `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리</span>

- diff 뷰어를 열어 최대 3개의 파일을 비교해보기:

`idea diff `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1 경로/대상/파일2 경로/대상/선택적_파일3</span>

- 양방향 파일 병합을 수행하려면, 병합 대화상자를 열기:

`idea merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>

- 프로젝트에서 코드 검사를 실행:

`idea inspect `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/프로젝트_디렉터리</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/조사_프로파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>
