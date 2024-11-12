---
layout: page
title: linux/sfdisk (한국어)
description: "디스크 파티션 테이블을 표시하거나 조작합니다."
content_hash: ae654bb69d9bf970eb764068aad0357d4a1b0683
last_modified_at: 2024-11-12
related_topics:
  - title: English version
    url: /en/linux/sfdisk.html
    icon: bi bi-globe
tldri18n_status: 2
---
# sfdisk

디스크 파티션 테이블을 표시하거나 조작합니다.
더 많은 정보: <https://manned.org/sfdisk>.

- 파티션 레이아웃을 파일로 백업:

`sudo sfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--dump</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dump</span>

- 파티션 레이아웃 복원:

`sudo sfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>` < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.dump</span>

- 파티션 유형 설정:

`sfdisk --part-type `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치}</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_번호</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">swap</span>

- 파티션 삭제:

`sfdisk --delete `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/장치</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_번호</span>

- 도움말 표시:

`sfdisk `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
