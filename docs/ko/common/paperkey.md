---
layout: page
title: common/paperkey (한국어)
description: "OpenPGP 키 아카이버."
content_hash: fb1e1f85217dd48db54bf90aca977ef327bbb3ff
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/paperkey.html
    icon: bi bi-globe
tldri18n_status: 2
---
# paperkey

OpenPGP 키 아카이버.
더 많은 정보: <https://www.jabberwocky.com/software/paperkey/>.

- 특정 비밀 키를 가져와 비밀 데이터를 포함한 텍스트 파일 생성:

`paperkey --secret-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀_키.gpg</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀_데이터.txt</span>

- `secret_data.txt`에 있는 비밀 키 데이터를 가져와 공개 키와 결합하여 비밀 키 재구성:

`paperkey --pubring `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/공개_키.gpg</span>` --secrets `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀_데이터.txt</span>` --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀_키.gpg</span>

- 특정 비밀 키를 내보내고 비밀 데이터를 포함한 텍스트 파일 생성:

`gpg --export-secret-key `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">키</span>` | paperkey --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/비밀_데이터.txt</span>
