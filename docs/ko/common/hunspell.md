---
layout: page
title: common/hunspell (한국어)
description: "철자 확인."
content_hash: c3fbb767eef80c834be3f9b874c92e6811f6c387
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/hunspell.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/hunspell.html
    icon: bi bi-globe
tldri18n_status: 2
---
# hunspell

철자 확인.
더 많은 정보: <https://github.com/hunspell/hunspell>.

- 파일의 철자를 확인:

`hunspell `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- en_US 사전을 사용하여 파일의 철자를 확인:

`hunspell -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">en_US</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 파일에 철자가 틀린 단어를 나열:

`hunspell -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
