---
layout: page
title: common/redis-cli (한국어)
description: "Redis 서버에 연결합니다."
content_hash: 3c21764c2225fe6eed6a0c31dea0abfaa30ba163
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/redis-cli.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/redis-cli.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># redis-cli

Redis 서버에 연결합니다.
더 많은 정보: <https://redis.io/topics/rediscli>.

- 로컬 서버에 연결:

`redis-cli`

- 기본 포트(6379)로 원격 서버에 연결:

`redis-cli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>

- 포트 번호를 지정하여 원격 서버에 연결:

`redis-cli -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>

- URI를 지정하여 원격 서버에 연결:

`redis-cli -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">URI</span>

- 비밀번호 지정:

`redis-cli -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- Redis 명령 실행:

`redis-cli `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">redis_명령</span>

- 로컬 클러스터에 연결:

`redis-cli -c`
