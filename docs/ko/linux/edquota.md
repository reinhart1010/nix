---
layout: page
title: linux/edquota (한국어)
description: "사용자 또는 그룹의 쿼터를 편집. 기본적으로 쿼터가 있는 모든 파일 시스템에서 작동합니다."
content_hash: 32434b1bda2cbbc1d137e073d1b87dc52f669393
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/edquota.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/edquota.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># edquota

사용자 또는 그룹의 쿼터를 편집. 기본적으로 쿼터가 있는 모든 파일 시스템에서 작동합니다.
쿼터 정보는 파일 시스템의 루트에 있는 `quota.user` 및 `quota.group` 파일에 영구적으로 저장됩니다.
더 많은 정보: <https://manned.org/edquota>.

- 현재 사용자의 쿼터 편집:

`edquota --user $(whoami)`

- 특정 사용자의 쿼터 편집:

`sudo edquota --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">사용자명</span>

- 그룹의 쿼터 편집:

`sudo edquota --group `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">그룹</span>

- 지정된 파일 시스템으로 작업 제한 (기본적으로 edquota는 쿼터가 있는 모든 파일 시스템에서 작동합니다):

`sudo edquota --file-system `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일_시스템</span>

- 기본 유예 기간 편집:

`sudo edquota -t`

- 다른 사용자에게 쿼터 복제:

`sudo edquota -p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">참조_사용자</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_사용자1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">대상_사용자2</span>
