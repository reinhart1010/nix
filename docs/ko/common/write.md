---
layout: page
title: common/write (한국어)
description: "지정된 로그인 사용자에게 터미널에 메시지를 작성합니다 (ctrl-C로 메시지 작성을 중단할 수 있음)."
content_hash: dd7de7c1e9bed0ff8fc3f5c39f861cf85c6ddf97
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/write.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/write.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/write.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># write

지정된 로그인 사용자에게 터미널에 메시지를 작성합니다 (ctrl-C로 메시지 작성을 중단할 수 있음).
시스템에서 활성 사용자들의 모든 터미널 ID를 확인하려면 `who` 명령을 사용하세요. 같이 보기: `mesg`.
더 많은 정보: <https://manned.org/write>.

- 지정된 사용자에게 주어진 터미널 ID로 메시지 전송:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자_명</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">터미널_ID</span>

- 터미널 `/dev/tty/5`에서 "testuser"에게 메시지 전송:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">testuser</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty/5</span>

- 의사 터미널 `/dev/pts/5`에서 "johndoe"에게 메시지 전송:

`write `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">johndoe</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pts/5</span>
