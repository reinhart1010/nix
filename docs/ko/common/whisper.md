---
layout: page
title: common/whisper (한국어)
description: "오디오 파일을 `txt`, `vtt`, `srt`, `tsv`, `json`으로 변환."
content_hash: 4e5a193e6c54bedd0b8ce2facd4e74cb2f588826
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/whisper.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/whisper.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># whisper

오디오 파일을 `txt`, `vtt`, `srt`, `tsv`, `json`으로 변환.
더 많은 정보: <https://github.com/openai/whisper>.

- 특정 오디오 파일을 모든 제공된 파일 형식으로 변환:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>

- 변환된 파일의 출력 형식을 지정하여 오디오 파일 변환:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>` --output_format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">txt</span>

- 특정 모델을 사용하여 오디오 파일 변환:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>` --model `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tiny.en,tiny,base.en,base,small.en,small,medium.en,medium,large-v1,large-v2,large</span>

- 오디오 파일의 언어를 지정하여 변환 시간을 단축하며 오디오 파일 변환:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>` --language `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">english</span>

- 오디오 파일을 변환하고 특정 위치에 저장:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>` --output_dir "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력</span>`"`

- 조용한 모드로 오디오 파일 변환:

`whisper `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/오디오.mp3</span>` --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">False</span>
