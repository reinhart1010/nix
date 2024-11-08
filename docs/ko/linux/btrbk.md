---
layout: page
title: linux/btrbk (한국어)
description: "btrfs 서브볼륨의 스냅샷 및 원격 백업 생성."
content_hash: 8cd83d7fcc8f264708494ce1f93fbe21a32c8e97
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/btrbk.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/btrbk.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># btrbk

btrfs 서브볼륨의 스냅샷 및 원격 백업 생성.
더 많은 정보: <https://digint.ch/btrbk/doc/readme.html>.

- 구성된 서브볼륨 및 스냅샷에 대한 통계 출력:

`sudo btrbk stats`

- 구성된 서브볼륨 및 스냅샷 나열:

`sudo btrbk list`

- 표시된 변경 사항 없이 실행 시 어떤 일이 발생할지 출력:

`sudo btrbk --verbose dryrun`

- 백업 루틴을 자세히 실행하고 진행 막대 표시:

`sudo btrbk --progress --verbose run`

- 구성된 서브볼륨에 대해 스냅샷만 생성:

`sudo btrbk snapshot`
