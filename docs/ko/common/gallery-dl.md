---
layout: page
title: common/gallery-dl (한국어)
description: "여러 이미지 호스팅 사이트에서 이미지 갤러리와 컬렉션 다운로드."
content_hash: e0bd13db46953dade06b95a02735e2496a492cd0
last_modified_at: 2024-10-21
related_topics:
  - title: English version
    url: /en/common/gallery-dl.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gallery-dl

여러 이미지 호스팅 사이트에서 이미지 갤러리와 컬렉션 다운로드.
더 많은 정보: <https://github.com/mikf/gallery-dl>.

- 지정된 URL에서 이미지 다운로드:

`gallery-dl "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">url</span>`"`

- 웹 브라우저에서 기존 쿠키를 검색 (로그인이 필요한 사이트에 유용):

`gallery-dl --cookies-from-browser `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">browser</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>`"`

- 사용자 이름과 비밀번호를 사용하여 인증을 지원하는 사이트에서 이미지의 직접 URL을 가져옴:

`gallery-dl --get-urls --username `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>` "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>`"`

- 장 번호와 언어별로 만화 장을 필터링:

`gallery-dl --chapter-filter "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10 <= chapter < 20</span>`" --option "lang=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">언어_코드</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">주소</span>`"`
