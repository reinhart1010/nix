---
layout: page
title: common/aspell (한국어)
description: "대화형 맞춤법 검사기."
content_hash: b11d842bf4d9c7118a9b274582c96aa5ee335914
last_modified_at: 2024-09-10
related_topics:
  - title: Deutsch version
    url: /de/common/aspell.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/aspell.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/aspell.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/common/aspell.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/aspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/aspell.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/aspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# aspell

대화형 맞춤법 검사기.
더 많은 정보: <http://aspell.net/>.

- 단일 파일의 철자 검사:

`aspell check `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`에서 철자가 틀린 단어를 나열:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | aspell list`

- 사용 가능한 사전적 언어 표시:

`aspell dicts`

- 다른 언어로 `aspell`을 실행 (두 글자 ISO 639 언어 코드 사용):

`aspell --lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cs</span>

- `stdin`에서 철자가 틀린 단어를 나열하고, 개인 단어 목록에서 단어를 무시:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` | aspell --personal=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">personal-word-list.pws</span>` list`
