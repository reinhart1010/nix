---
layout: page
title: common/satis (한국어)
description: "Satis 정적 Composer 저장소를 위한 명령줄 도구."
content_hash: f148c0dc8852f0aa77826cbcf499a5230b1c6ecd
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/satis.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/satis.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># satis

Satis 정적 Composer 저장소를 위한 명령줄 도구.
더 많은 정보: <https://github.com/composer/satis>.

- Satis 구성 초기화:

`satis init `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">satis.json</span>

- Satis 구성에 VCS 저장소 추가:

`satis add `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_주소</span>

- 구성에서 정적 출력 생성:

`satis build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">satis.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>

- 지정된 저장소만 업데이트하여 정적 출력 생성:

`satis build --repository-url `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">저장소_주소</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">satis.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>

- 불필요한 아카이브 파일 제거:

`satis purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">satis.json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력_폴더</span>
