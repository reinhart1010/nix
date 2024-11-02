---
layout: page
title: common/ssh-keyscan (한국어)
description: "원격 호스트의 공개 SSH 키를 가져옵니다."
content_hash: 224bd21b28db16f758974fcde1aab900f405b69d
last_modified_at: 2024-11-02
related_topics:
  - title: Deutsch version
    url: /de/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/ssh-keyscan.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/ssh-keyscan.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ssh-keyscan

원격 호스트의 공개 SSH 키를 가져옵니다.
더 많은 정보: <https://man.openbsd.org/ssh-keyscan>.

- 원격 호스트의 모든 공개 SSH 키 가져오기:

`ssh-keyscan `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 특정 포트에서 대기 중인 원격 호스트의 모든 공개 SSH 키 가져오기:

`ssh-keyscan -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 원격 호스트의 특정 유형의 공개 SSH 키 가져오기:

`ssh-keyscan -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">rsa,dsa,ecdsa,ed25519</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 주어진 호스트의 지문으로 SSH known_hosts 파일 수동 업데이트:

`ssh-keyscan -H `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` >> ~/.ssh/known_hosts`
