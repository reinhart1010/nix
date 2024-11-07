---
layout: page
title: common/mu (한국어)
description: "로컬 Maildir에서 이메일을 색인하고 검색."
content_hash: 29d9542e1ba3dff161df9bc38abf650712551108
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/mu.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/mu.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mu

로컬 Maildir에서 이메일을 색인하고 검색.
더 많은 정보: <https://man.cx/mu>.

- 이메일 데이터베이스 초기화, 선택적으로 Maildir 디렉토리와 이메일 주소 지정:

`mu init --maildir=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>` --my-address=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name@example.com</span>

- 새로운 이메일 색인:

`mu index`

- 특정 키워드를 사용하여 메시지 찾기 (메시지 본문, 제목, 발신자 등):

`mu find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키워드</span>

- Alice에게 보낸 메시지 중 제목이 `jellyfish`이고 본문에 `apples` 또는 `oranges`가 포함된 메시지 찾기:

`mu find to:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">alice</span>` subject:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">jellyfish</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">apples</span>` OR `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">oranges</span>

- 보낸 편지함에 있는, `soc`로 시작하는 단어에 대한 읽지 않은 메시지 찾기 (`*`는 검색어 끝에서만 작동):

`mu find 'subject:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">soc</span>`*' flag:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unread</span>` maildir:'/`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Sent Items</span>`'`

- Sam에게서 온, 이미지가 첨부된 2 KiB에서 2 MiB 사이의 크기로 2021년에 작성된 메시지 찾기:

`mu find 'mime:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image/*</span>` size:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">2k..2m</span>` date:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">20210101..20211231</span>` from:`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sam</span>

- 이름 또는 이메일 주소에 `Bob`이 포함된 연락처 나열:

`mu cfind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Bob</span>
