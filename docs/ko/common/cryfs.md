---
layout: page
title: common/cryfs (한국어)
description: "클라우드용 암호화 파일 시스템."
content_hash: 7705792c8100dc57b1bc7b270b6d463951b5ecf2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cryfs.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cryfs

클라우드용 암호화 파일 시스템.
더 많은 정보: <https://www.cryfs.org/>.

- 암호화 된 파일 시스템 마운트. 초기화 마법사는 처음 실행될 때 시작:

`cryfs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cipher_dir/의/경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트/의/경로</span>

- 암호화 된 파일 시스템 마운트 해제:

`cryfs-unmount `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트/의/경로</span>

- 10분 동안 활동이 없으면 자동으로 마운트 해제:

`cryfs --unmount-idle `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cipher_dir/의/경로</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_포인트/의/경로</span>

- 지원되는 암호 목록 표시:

`cryfs --show-ciphers`
