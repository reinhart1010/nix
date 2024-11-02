---
layout: page
title: common/tlmgr-key (한국어)
description: "TeX Live 데이터베이스를 검증하는 데 사용되는 GPG 키 관리."
content_hash: f7e77868a739fdfcb93552e31b3e0dc309daca1a
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/tlmgr-key.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tlmgr key

TeX Live 데이터베이스를 검증하는 데 사용되는 GPG 키 관리.
더 많은 정보: <https://www.tug.org/texlive/tlmgr.html>.

- TeX Live의 모든 키 나열:

`tlmgr key list`

- 특정 파일에서 키 추가:

`sudo tlmgr key add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.gpg</span>

- `stdin`에서 키 추가:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키.gpg</span>` | sudo tlmgr key add -`

- ID로 특정 키 제거:

`sudo tlmgr key remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키_ID</span>
