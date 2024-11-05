---
layout: page
title: common/john (한국어)
description: "비밀번호 크래커."
content_hash: 112db3d49bbca6bbe7e1d0433983a56fd1e345a9
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/john.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/john.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/john.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># john

비밀번호 크래커.
더 많은 정보: <https://www.openwall.com/john/>.

- 비밀번호 해시 크래킹:

`john `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들.txt</span>

- 크래킹된 비밀번호 표시:

`john --show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들.txt</span>

- 여러 파일에서 사용자 식별자로 크래킹된 비밀번호 표시:

`john --show --users=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_ID들</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들1.txt 경로/대상/해시들2.txt ...</span>

- 사용자 정의 워드리스트를 사용하여 비밀번호 해시 크래킹:

`john --wordlist=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/워드리스트.txt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들.txt</span>

- 사용 가능한 해시 형식 나열:

`john --list=formats`

- 특정 해시 형식을 사용하여 비밀번호 해시 크래킹:

`john --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">md5crypt</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들.txt</span>

- 단어 변형 규칙을 활성화하여 비밀번호 해시 크래킹:

`john --rules `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/해시들.txt</span>

- 중단된 크래킹 세션을 상태 파일에서 복구, 예: `mycrack.rec`:

`john --restore=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/mycrack.rec</span>
