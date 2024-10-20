---
layout: page
title: common/ffplay (한국어)
description: "FFmpeg 라이브러리와 SDL 라이브러리를 사용하는 간단하고 휴대 간으한 미디어 플레이어."
content_hash: 58aa77b9728047cd7a7f35f2cb52dd07f4def1b3
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/ffplay.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ffplay.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ffplay

FFmpeg 라이브러리와 SDL 라이브러리를 사용하는 간단하고 휴대 간으한 미디어 플레이어.
더 많은 정보: <https://ffmpeg.org/ffplay-all.html>.

- 미디어 파일 재생:

`ffplay `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- GUI 없이 미디어 파일에서 오디오 재생:

`ffplay -nodisp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- `stdin`을 통해 `ffmpeg`에 의해 전달된 미디어 재생:

`ffmpeg -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>` -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">copy</span>` -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">미디어_포맷</span>` - | ffplay -`

- 실시간으로 비디오를 재생하고 모션 벡터를 표시:

`ffplay -flags2 +export_mvs -vf codecview=mv=pf+bf+bb `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>

- 비디오 키프레임만 표시:

`ffplay -vf select="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">eq(pict_type\,PICT_TYPE_I)</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일</span>
