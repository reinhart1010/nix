---
layout: page
title: common/xgettext (한국어)
description: "코드 파일에서 gettext 문자열 추출."
content_hash: 37e3702026ac9e9f28e98928e6ba25f2ff0087eb
last_modified_at: 2024-11-06
related_topics:
  - title: English version
    url: /en/common/xgettext.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xgettext

코드 파일에서 gettext 문자열 추출.
더 많은 정보: <https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html>.

- 파일을 스캔하고 문자열을 `messages.po`에 출력:

`xgettext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 다른 출력 파일 이름 사용:

`xgettext --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 새 문자열을 기존 파일에 추가:

`xgettext --join-existing --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_파일</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 메타데이터를 포함하는 헤더를 출력 파일에 추가하지 않음:

`xgettext --omit-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>
