---
layout: page
title: linux/fscrypt (한국어)
description: "Linux 파일 시스템 암호화를 관리하는 Go 도구."
content_hash: efab9b146aed7c103ef9575255c8c19b068d78fd
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/fscrypt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# fscrypt

Linux 파일 시스템 암호화를 관리하는 Go 도구.
더 많은 정보: <https://github.com/google/fscrypt>.

- fscrypt를 사용하기 위해 루트 파일 시스템 준비:

`fscrypt setup`

- 디렉터리에 파일 시스템 암호화 활성화:

`fscrypt encrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 암호화된 디렉터리 잠금 해제:

`fscrypt unlock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_폴더</span>

- 암호화된 디렉터리 잠금:

`fscrypt lock `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/암호화된_폴더</span>
