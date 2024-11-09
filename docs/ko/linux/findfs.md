---
layout: page
title: linux/findfs (한국어)
description: "파일시스템을 레이블 또는 UUID로 찾습니다."
content_hash: 1a245099f12685de21ec2e1acf37fbff02f323ea
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/findfs.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/findfs.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># findfs

파일시스템을 레이블 또는 UUID로 찾습니다.
더 많은 정보: <https://mirrors.edge.kernel.org/pub/linux/utils/util-linux>.

- 파일시스템 레이블로 블록 장치 검색:

`findfs LABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">레이블</span>

- 파일시스템 UUID로 검색:

`findfs UUID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uuid</span>

- 파티션 레이블로 검색 (GPT 또는 MAC 파티션 테이블):

`findfs PARTLABEL=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_레이블</span>

- 파티션 UUID로 검색 (GPT 파티션 테이블 전용):

`findfs PARTUUID=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파티션_uuid</span>
