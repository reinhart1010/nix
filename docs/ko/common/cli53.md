---
layout: page
title: common/cli53 (한국어)
description: "Amazon Route 53용 명령줄 도구."
content_hash: 9d6bead8d9b6abf88cee292a1e409bed6090f61c
last_modified_at: 2024-10-04
related_topics:
  - title: English version
    url: /en/common/cli53.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cli53

Amazon Route 53용 명령줄 도구.
더 많은 정보: <https://github.com/barnybug/cli53>.

- 도메인 나열:

`cli53 list`

- 도메인 생성:

`cli53 create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>` --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">코멘트</span>`"`

- 바인드 존 파일을 `stdout`으로 내보내기:

`cli53 export `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>

- 동일한 영역의 상대 레코드를 가리키는 `www` 하위 도메인을 생성:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 CNAME lb'</span>

- 외부 주소를 가리키는 `www` 하위 도메인을 생성 (점으로 끝나야 함):

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 CNAME lb.externalhost.com.'</span>

- IP 주소를 가리키는 `www` 하위 도메인을 생성:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 A 150.130.110.1'</span>

- 다른 IP를 가리키는 `www` 하위 도메인을 교체:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rc|rrcreate</span>` --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">'www 300 A 150.130.110.2'</span>

- A 레코드 삭제:

`cli53 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rd|rrdelete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">도메인주소.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">www</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">A</span>
