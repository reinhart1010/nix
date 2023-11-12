---
layout: page
title: common/cpio (한국어)
description: "아카이브 안팎으로 파일을 복사. cpio의 custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, POSIX.1 tar.와 같은 아카이브 형식을 지원함."
content_hash: e716d9dc3aa65c22b9c1685da5d482a6227aa147
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/cpio.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cpio.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpio

아카이브 안팎으로 파일을 복사. cpio의 custom binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old tar, POSIX.1 tar.와 같은 아카이브 형식을 지원함.
더 많은 정보: <https://www.gnu.org/software/cpio>.

- 표준 입력에서 파일 이름 목록을 가져와서 cpio의 이진 형식으로 아카이브[o]에 추가:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일2</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">파일3</span>`" | cpio -o > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>

- 디렉토리의 모든 파일과 디렉토리를 복사하여 [v]상세모드에서 아카이브[o]에 추가:

`find `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">디렉토리/의/경로</span>` | cpio -ov > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>

- 아카이브에 모든 파일을 [i]선택하여 필요한 경우 [v]상세모드로 [d]디렉토리를 생성:

`cpio -idv < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archive.cpio</span>
