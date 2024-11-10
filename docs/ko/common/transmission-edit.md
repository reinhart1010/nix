---
layout: page
title: common/transmission-edit (한국어)
description: "토렌트 파일에서 announce URL을 수정."
content_hash: b07bc41b791234711cdc7a429c05a98302b97e17
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/transmission-edit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/transmission-edit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/transmission-edit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# transmission-edit

토렌트 파일에서 announce URL을 수정.
같이 보기: `transmission`.
더 많은 정보: <https://manned.org/transmission-edit>.

- 토렌트의 announce 목록에 URL 추가 또는 삭제:

`transmission-edit --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">add|delete</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">http://example.com</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.torrent</span>

- 토렌트 파일에서 트래커의 패스코드 업데이트:

`transmission-edit --replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">기존-패스코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새로운-패스코드</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.torrent</span>
