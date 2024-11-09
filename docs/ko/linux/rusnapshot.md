---
layout: page
title: linux/rusnapshot (한국어)
description: "Rust로 작성된 BTRFS 스냅샷 유틸리티."
content_hash: 3b0583c66ba1c4fb82fe0ab8bb738422d448b8fc
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/rusnapshot.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/rusnapshot.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># rusnapshot

Rust로 작성된 BTRFS 스냅샷 유틸리티.
더 많은 정보: <https://github.com/Edu4rdSHL/rusnapshot>.

- 구성 파일을 사용하여 스냅샷 생성:

`sudo rusnapshot --config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --cr`

- 생성된 스냅샷 나열:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --list`

- ID 또는 스냅샷 이름으로 스냅샷 삭제:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --del --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_id</span>

- 모든 `hourly` 스냅샷 삭제:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --list --keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0</span>` --clean --kind `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hourly</span>

- 읽기-쓰기 스냅샷 생성:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --cr --rw`

- 스냅샷 복원:

`sudo rusnapshot -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/config.toml</span>` --id `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_id</span>` --restore`
