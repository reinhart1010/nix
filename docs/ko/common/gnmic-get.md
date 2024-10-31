---
layout: page
title: common/gnmic-get (한국어)
description: "gnmi 네트워크 장치 작동 데이터의 스냅샷 가져오기."
content_hash: 9c077bf430a6d1402d42a24aafb19c3fad89075d
last_modified_at: 2024-10-31
related_topics:
  - title: English version
    url: /en/common/gnmic-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gnmic get

gnmi 네트워크 장치 작동 데이터의 스냅샷 가져오기.
더 많은 정보: <https://gnmic.kmrd.dev/cmd/get>.

- 특정 경로에서 장치 상태의 스냅샷을 가져옴:

`gnmic --address `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>

- 여러 경로에서 장치 상태를 쿼리:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리2</span>

- 공통 접두사를 사용하여 여러 경로에서 장치 상태를 쿼리:

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` get --prefix `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">접두사</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리1</span>` --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉터리2</span>

- 장치 상태를 쿼리하고 응답 인코딩을 지정 (json_ietf):

`gnmic -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아이피:포트</span>` get --path `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로</span>` --encoding json_ietf`
