---
layout: page
title: common/restic (한국어)
description: "빠르고 안전한 백업 프로그램."
content_hash: 55bbdb5d701b8dcea3537f4e51988fc02eb1d6be
last_modified_at: 2024-11-07
related_topics:
  - title: English version
    url: /en/common/restic.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/restic.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># restic

빠르고 안전한 백업 프로그램.
더 많은 정보: <https://restic.net>.

- 지정된 로컬 디렉터리에 백업 저장소 초기화:

`restic init --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>

- 디렉터리를 저장소에 백업:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 저장소에 현재 저장된 백업 스냅샷 표시:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` snapshots`

- 특정 백업 스냅샷을 대상 디렉터리에 복원:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">latest|스냅샷_ID</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>

- 특정 백업의 특정 경로를 대상 디렉터리에 복원:

`restic --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/저장소</span>` restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_ID</span>` --target `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/타겟</span>` --include `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/복원</span>

- 저장소를 정리하고 각 고유 백업의 최신 스냅샷만 유지:

`restic forget --keep-last 1 --prune`
