---
layout: page
title: common/zfs (한국어)
description: "ZFS 파일 시스템 관리."
content_hash: 25aacdb25a8c9aeab2d625b65438f9804fa1c740
last_modified_at: 2024-11-01
related_topics:
  - title: English version
    url: /en/common/zfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/zfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># zfs

ZFS 파일 시스템 관리.
더 많은 정보: <https://manned.org/zfs>.

- 사용 가능한 모든 ZFS 파일 시스템 나열:

`zfs list`

- 새 ZFS 파일 시스템 생성:

`zfs create `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름/파일시스템_이름</span>

- ZFS 파일 시스템 삭제:

`zfs destroy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름/파일시스템_이름</span>

- ZFS 파일 시스템의 스냅샷 생성:

`zfs snapshot `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름/파일시스템_이름</span>`@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_이름</span>

- 파일 시스템에 압축 활성화:

`zfs set compression=on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름/파일시스템_이름</span>

- 파일 시스템의 마운트 포인트 변경:

`zfs set mountpoint=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/my/mount/path</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">풀_이름/파일시스템_이름</span>
