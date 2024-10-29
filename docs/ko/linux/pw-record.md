---
layout: page
title: linux/pw-record (한국어)
description: "PipeWire를 통해 오디오 파일을 녹음."
content_hash: 04a8eb08847dca550eed7763bcc5c9580081c5fb
last_modified_at: 2024-10-29
related_topics:
  - title: English version
    url: /en/linux/pw-record.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pw-record.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pw-record.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pw-record.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pw-record

PipeWire를 통해 오디오 파일을 녹음.
`pw-cat --record`의 축약형.
더 많은 정보: <https://fedoraproject.org/wiki/QA:Testcase_PipeWire_PipeWire_CLI>.

- 기본 대상 장치를 사용하여 샘플 녹음:

`pw-record `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 다른 볼륨 레벨로 샘플 녹음:

`pw-record --volume=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.1</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>

- 다른 샘플 속도를 사용하여 샘플 녹음:

`pw-record --rate=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">6000</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.wav</span>
