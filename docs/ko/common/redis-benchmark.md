---
layout: page
title: common/redis-benchmark (한국어)
description: "Redis 서버의 성능을 테스트."
content_hash: 4701fd0d0f8c03e61d4f55c493d5c6e0d26746cb
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/redis-benchmark.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/redis-benchmark.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># redis-benchmark

Redis 서버의 성능을 테스트.
더 많은 정보: <https://redis.io/docs/latest/operate/oss_and_stack/management/optimization/benchmarks/>.

- 전체 벤치마크 실행:

`redis-benchmark`

- 특정 Redis 서버에서 벤치마크 실행:

`redis-benchmark -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 기본 100000 요청으로 테스트의 일부 실행:

`redis-benchmark -h `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">호스트</span>` -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">포트</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set,lpush</span>` -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>

- 특정 스크립트로 실행:

`redis-benchmark -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>` script load "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">redis.call('set', 'foo', 'bar')</span>`"`

- 100000개의 [r]andom 키를 사용하여 벤치마크 실행:

`redis-benchmark -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set</span>` -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">100000</span>

- 16개의 명령으로 [P]ipelining하여 벤치마크 실행:

`redis-benchmark -n `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1000000</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">set,get</span>` -P `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">16</span>

- [q]uietly 실행하여 초당 쿼리 결과만 표시:

`redis-benchmark -q`
