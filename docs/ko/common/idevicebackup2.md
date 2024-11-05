---
layout: page
title: common/idevicebackup2 (한국어)
description: "iOS 4 이상을 실행하는 장치에 대한 백업을 생성하거나 복원."
content_hash: 4b9ae8be13bc1362a19233cfc40527353e1ab467
last_modified_at: 2024-11-05
related_topics:
  - title: English version
    url: /en/common/idevicebackup2.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/idevicebackup2.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># idevicebackup2

iOS 4 이상을 실행하는 장치에 대한 백업을 생성하거나 복원.
더 많은 정보: <https://manned.org/idevicebackup2>.

- 지정된 디렉터리에 장치의 백업을 생성:

`idevicebackup2 backup `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 지정된 디렉터리에서 백업을 복원:

`idevicebackup2 restore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/디렉터리</span>

- 백업 암호화 활성화:

`idevicebackup2 encryption on `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">비밀번호</span>

- 마지막으로 완료된 백업의 파일을 나열:

`idevicebackup2 list`
