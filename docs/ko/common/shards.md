---
layout: page
title: common/shards (한국어)
description: "Crystal 언어를 위한 의존성 관리 도구."
content_hash: 95fc026d624a8d27181d26fc3baeac6f5df4ea7a
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/shards.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/shards.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/shards.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># shards

Crystal 언어를 위한 의존성 관리 도구.
더 많은 정보: <https://crystal-lang.org/reference/the_shards_command>.

- `shard.yml` 파일의 기본 골격 생성:

`shards init`

- `shard.yml` 파일에서 의존성 설치:

`shards install`

- 모든 의존성 업데이트:

`shards update`

- 설치된 모든 의존성 나열:

`shards list`

- 의존성의 버전 표시:

`shards version `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/의존성_폴더</span>
