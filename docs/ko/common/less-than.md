---
layout: page
title: common/less-than (한국어)
description: "데이터를 `stdin`으로 리다이렉트."
content_hash: 95a0cc81a85e48b38acdfc306462517902b1ec6a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/less-than.html
    icon: bi bi-globe
tldri18n_status: 2
---
# Less than

데이터를 `stdin`으로 리다이렉트.
더 많은 정보: <https://gnu.org/software/bash/manual/bash.html#Redirecting-Input>.

- 파일을 `stdin`으로 리다이렉트 (`cat file.txt |`와 동일한 효과를 가짐):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.txt</span>

- 히어 문서를 생성하여 `stdin`으로 전달 (여러 줄 명령 필요):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` << `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EOF</span>` <Enter> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">여러_줄_데이터</span>` <Enter> `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">EOF</span>

- 히어 문자열을 생성하여 `stdin`으로 전달 (`echo string |`와 동일한 효과를 가짐):

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` <<< `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">문자열</span>
