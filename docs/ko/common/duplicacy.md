---
layout: page
title: common/duplicacy (한국어)
description: "잠금 없는 중복 제거 클라우드 백업 도구."
content_hash: 6ee34fda857987dae8b321241b9cd16c623c6cc2
last_modified_at: 2024-10-16
related_topics:
  - title: English version
    url: /en/common/duplicacy.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/duplicacy.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># duplicacy

잠금 없는 중복 제거 클라우드 백업 도구.
더 많은 정보: <https://github.com/gilbertchen/duplicacy/wiki>.

- 현재 디레터리를 저장소로 사용하고, SFTP 저장소를 초기화하고, 저장소를 비밀번호로 암호화:

`duplicacy init -e `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">snapshot_id</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sftp://user@192.168.2.100/path/to/storage/</span>

- 저장소의 스냅샷을 기본 저장소에 저장:

`duplicacy backup`

- 현재 저장소의 스냅샷 목록:

`duplicacy list`

- 이전에 저장된 스냅샷으로 저장소를 복원:

`duplicacy restore -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">revision</span>

- 스냅샷의 무결성을 확인:

`duplicacy check`

- 기존 저장소에 사용할 다른 저장소를 추가:

`duplicacy add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스냅샷_아이디</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">스토리지_주소</span>

- 스냅샷의 특정 버전을 정리:

`duplicacy prune -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">버전</span>

- `m`일보다 오래된 버전에 대해 `n`일마다 하나의 업데이트된 버전을 유지하여 버전을 정리:

`duplicacy prune -keep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n:m</span>
