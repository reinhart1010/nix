---
layout: page
title: linux/ntpdate (한국어)
description: "NTP를 통해 날짜 및 시간을 동기화하고 설정합니다."
content_hash: 56a167b5bc38a1f0f3a5779c478b5bf2ba9a3f2e
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/linux/ntpdate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ntpdate

NTP를 통해 날짜 및 시간을 동기화하고 설정합니다.
더 많은 정보: <https://manned.org/ntpdate>.

- 날짜와 시간을 동기화하고 설정:

`sudo ntpdate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 시간을 설정하지 않고 호스트에 질의:

`ntpdate -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 방화벽이 특권 포트를 차단하는 경우 비특권 포트를 사용:

`sudo ntpdate -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 시간을 `slewed` 대신 `settimeofday`를 사용하여 강제로 조정:

`sudo ntpdate -b `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>
