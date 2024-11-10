---
layout: page
title: common/tidy (한국어)
description: "HTML, XHTML 및 XML 파일을 정리하고 보기 좋게 출력."
content_hash: c476836603c7f37a7cc764710811986de869d097
last_modified_at: 2024-11-10
related_topics:
  - title: English version
    url: /en/common/tidy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# tidy

HTML, XHTML 및 XML 파일을 정리하고 보기 좋게 출력.
참고: `tidy`는 원래 들여쓰기를 보존할 수 없습니다.
더 많은 정보: <https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>.

- HTML 파일을 보기 좋게 출력:

`tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>

- [i]ndentation을 활성화하고, 줄을 100으로 [w]rapping하여 `output.html`에 저장:

`tidy --indent y --wrap 100 -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/output.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>

- 설정 파일을 사용하여 HTML 파일을 직접 수정:

`tidy -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/설정</span>` -modify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">경로/대상/파일.html</span>
