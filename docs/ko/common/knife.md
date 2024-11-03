---
layout: page
title: common/knife (한국어)
description: "로컬 Chef 저장소에서 Chef 서버와 상호 작용."
content_hash: 6a8c3596c0e571a9aee8efaafc87c5a474f05f29
last_modified_at: 2024-11-03
related_topics:
  - title: English version
    url: /en/common/knife.html
    icon: bi bi-globe
tldri18n_status: 2
---
# knife

로컬 Chef 저장소에서 Chef 서버와 상호 작용.
더 많은 정보: <https://docs.chef.io/knife.html>.

- 새 노드 부트스트랩:

`knife bootstrap `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">fqdn_또는_ip</span>

- 등록된 모든 노드 나열:

`knife node list`

- 노드 표시:

`knife node show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>

- 노드 편집:

`knife node edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">노드_이름</span>

- 역할 편집:

`knife role edit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">역할_이름</span>

- 데이터 백 보기:

`knife data bag show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_백_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">데이터_백_항목</span>

- 로컬 쿠크북을 Chef 서버에 업로드:

`knife cookbook upload `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">쿠크북_이름</span>
