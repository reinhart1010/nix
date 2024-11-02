---
layout: page
title: common/zipalign (한국어)
description: "Zip 아카이브 정렬 도구."
content_hash: bdc8815b14d26850bd614b802041dcc4d9ada045
last_modified_at: 2024-11-02
related_topics:
  - title: English version
    url: /en/common/zipalign.html
    icon: bi bi-globe
tldri18n_status: 2
---
# zipalign

Zip 아카이브 정렬 도구.
Android SDK 빌드 도구의 일부.
더 많은 정보: <https://developer.android.com/tools/zipalign>.

- Zip 파일의 데이터를 4바이트 경계에 맞춰 정렬:

`zipalign `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.zip</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/출력.zip</span>

- Zip 파일이 4바이트 경계에 맞게 올바르게 정렬되었는지 확인하고 결과를 자세히 표시:

`zipalign -v -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">4</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/입력.zip</span>
