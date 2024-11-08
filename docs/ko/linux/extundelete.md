---
layout: page
title: linux/extundelete (한국어)
description: "저널을 분석하여 ext3 또는 ext4 파티션에서 삭제된 파일을 복구합니다."
content_hash: ac6ccebba7997801e0047b7a4c77a2707cdfdb51
last_modified_at: 2024-11-08
related_topics:
  - title: English version
    url: /en/linux/extundelete.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/extundelete.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># extundelete

저널을 분석하여 ext3 또는 ext4 파티션에서 삭제된 파일을 복구합니다.
Unix 시간 정보는 `date`, 파티션을 마운트 해제하려면 `umount`도 참조하세요.
더 많은 정보: <https://extundelete.sourceforge.net>.

- 디바이스 X의 파티션 N 안의 모든 삭제된 파일 복구:

`sudo extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-all`

- 루트에 상대적인 경로에서 파일 복구(경로를 `/`로 시작하지 마세요):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 루트에 상대적인 경로에서 폴더 복구(경로를 `/`로 시작하지 마세요):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-directory `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/폴더</span>

- 2020년 1월 1일 이후 삭제된 모든 파일 복구(Unix 시간 기준):

`extundelete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/dev/sdXN</span>` --restore-all --after `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1577840400</span>
