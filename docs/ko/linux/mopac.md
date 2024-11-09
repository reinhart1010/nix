---
layout: page
title: linux/mopac (한국어)
description: "MOPAC (Molecular Orbital PACkage)는 Dewar 및 Thiel의 NDDO 근사를 기반으로 한 반경험적 양자 화학 프로그램입니다."
content_hash: acb717d9d5c606ee7007797115369b8da0bfd988
last_modified_at: 2024-11-09
related_topics:
  - title: English version
    url: /en/linux/mopac.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/mopac.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/mopac.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># mopac

MOPAC (Molecular Orbital PACkage)는 Dewar 및 Thiel의 NDDO 근사를 기반으로 한 반경험적 양자 화학 프로그램입니다.
더 많은 정보: <https://github.com/openmopac/mopac>.

- 입력 파일(`.mop`, `.dat`, `.arc`)에 따라 계산 수행:

`mopac `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력_파일</span>

- 현재 디렉토리에 기록하고 출력 파일을 스트리밍하는 HF의 최소 작업 예제:

`touch test.out; echo "PM7\n#comment\n\nH 0.95506 0.05781 -0.03133\nF 1.89426 0.05781 -0.03133" > test.mop; mopac test.mop & tail -f test.out`
