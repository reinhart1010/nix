---
layout: page
title: common/tarsnap (한국어)
description: "원격 Tarsnap 암호화 백업을 조작."
content_hash: d8f20f32c889615030a3963cc860cb0376cef067
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/common/tarsnap.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/tarsnap.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># tarsnap

원격 Tarsnap 암호화 백업을 조작.
참고: `/usr/local/etc/tarsnap.conf` 또는 `~/.tarsnaprc`에서 설정하면 키 파일과 캐시 디렉토리를 지정할 필요가 없습니다.
같이 보기: `tarsnap-keygen`.
더 많은 정보: <https://www.tarsnap.com/man-tarsnap.1.html>.

- 하나 이상의 파일 또는 디렉토리에 대한 백업 아카이브 생성, 암호화 키와 캐시 디렉토리 지정:

`tarsnap -c --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` --cachedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/캐시_디렉토리</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 업로드될 데이터 양 표시:

`tarsnap -c --dry-run --print-stats --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` --cachedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/캐시_디렉토리</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 저장된 아카이브 목록 표시:

`tarsnap --list-archives --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>

- 특정 아카이브 삭제:

`tarsnap -d --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` --cachedir `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/캐시_디렉토리</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_이름</span>

- 특정 아카이브의 내용을 상세 모드로 목록화:

`tarsnap -tv --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_이름</span>

- 특정 아카이브에서 하나 이상의 파일 또는 디렉토리 복원:

`tarsnap -x --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">아카이브_이름</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일_또는_디렉토리1 경로/대상/파일_또는_디렉토리2 ...</span>

- 아카이브 복사:

`tarsnap -c --keyfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/키_파일</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">새_아카이브_이름</span>` @@`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">원본_아카이브_이름</span>
