---
layout: page
title: linux/quotacheck (한국어)
description: "파일 시스템의 디스크 사용량을 스캔하여 쿼터 파일을 생성, 확인 및 복구합니다."
content_hash: 2b8e5c83316807df481cd99997a6656a2940a888
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/quotacheck.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/quotacheck.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># quotacheck

파일 시스템의 디스크 사용량을 스캔하여 쿼터 파일을 생성, 확인 및 복구합니다.
쿼터 파일의 손상이나 손실을 방지하기 위해 쿼터를 비활성화한 상태에서 실행하는 것이 좋습니다.
더 많은 정보: <https://manned.org/quotacheck>.

- 모든 마운트된 비-NFS 파일 시스템의 쿼터 확인:

`sudo quotacheck --all`

- 쿼터가 활성화된 상태에서도 강제 확인 (쿼터 파일의 손상이나 손실이 발생할 수 있음):

`sudo quotacheck --force `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 디버그 모드로 주어진 파일 시스템의 쿼터 확인:

`sudo quotacheck --debug `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 진행 상황을 표시하며 주어진 파일 시스템의 쿼터 확인:

`sudo quotacheck --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 사용자 쿼터 확인:

`sudo quotacheck --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>

- 그룹 쿼터 확인:

`sudo quotacheck --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">마운트_지점</span>
