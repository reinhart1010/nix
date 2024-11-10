---
layout: page
title: linux/unshare (한국어)
description: "사용자 정의 네임스페이스에서 명령을 실행합니다."
content_hash: 8ae68f26cadc201af28a6e36087d0068641b401e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/unshare.html
    icon: bi bi-globe
tldri18n_status: 2
---
# unshare

사용자 정의 네임스페이스에서 명령을 실행합니다.
더 많은 정보: <https://www.kernel.org/doc/html/latest/userspace-api/unshare.html>.

- 연결된 네트워크에 대한 액세스를 공유하지 않고 명령 실행:

`unshare --net `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자들</span>

- 마운트, 프로세스, 네트워크를 공유하지 않고 자식 프로세스로 명령 실행:

`unshare --mount --pid --net --fork `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령어_인자들</span>
