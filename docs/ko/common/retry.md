---
layout: page
title: common/retry (한국어)
description: "명령이 성공하거나 기준이 충족될 때까지 명령을 반복."
content_hash: 2bf5b76e3db304a37de5721f9ecc4f8cf190321a
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/common/retry.html
    icon: bi bi-globe
tldri18n_status: 2
---
# retry

명령이 성공하거나 기준이 충족될 때까지 명령을 반복.
더 많은 정보: <https://github.com/minfrin/retry>.

- 명령이 성공할 때까지 재시도:

`retry `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- 명령이 성공할 때까지 n초마다 재시도:

`retry --delay=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>

- n번 시도 후 포기:

`retry --times=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">명령</span>
