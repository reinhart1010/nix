---
layout: page
title: common/gnmic-set (한국어)
description: "gnmi 네트워크 장치 구성을 수정."
content_hash: 8a0533328ab4d0dde14f41c18af016d97ceb3322
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gnmic-set.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnmic set

gnmi 네트워크 장치 구성을 수정.
더 많은 정보: <https://gnmic.kmrd.dev/cmd/set>.

- 경로의 값을 업데이트:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` set --update-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --update-value `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">값</span>

- JSON 파일의 내용과 일치하도록 경로 값을 업데이트:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` set --update-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --update-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일경로</span>

- JSON 파일의 내용과 일치하도록 경로 값을 변경:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` set --replace-path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --replace-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일경로</span>

- 주어진 경로에서 노드를 삭제:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` set --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>
