---
layout: page
title: common/notmuch (한국어)
description: "대량의 이메일 메시지를 색인화, 검색, 읽기 및 태깅하기 위한 명령줄 기반 프로그램."
content_hash: 57e19d0187db456655d9284f40af35cc77497e40
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/notmuch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# notmuch

대량의 이메일 메시지를 색인화, 검색, 읽기 및 태깅하기 위한 명령줄 기반 프로그램.
더 많은 정보: <https://notmuchmail.org/manpages/>.

- 초기 사용을 위한 설정:

`notmuch setup`

- 검색어와 일치하는 모든 메시지에 태그 추가:

`notmuch tag +`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_정의_태그</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`

- 검색어와 일치하는 모든 메시지의 태그 제거:

`notmuch tag -`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_정의_태그</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`

- 주어진 검색어와 일치하는 메시지 수 세기:

`notmuch count --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">messages|threads</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`

- 주어진 검색어와 일치하는 메시지 검색:

`notmuch search --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">summary|threads|messages|files|tags</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`

- 검색 결과를 X개로 제한:

`notmuch search --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">json|text</span>` --output=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">summary|threads|messages|files|tags</span>` --limit=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">X</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`

- 메시지 세트에 대한 회신 템플릿 생성:

`notmuch reply --format=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">default|headers-only</span>` --reply-to=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sender|all</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">검색_어구</span>`"`
