---
layout: page
title: common/crane-index-filter (Nederlands)
description: "Wijzigt een remote index door te filteren op basis van platform."
content_hash: c44e10cb9fba469c3c803cbb0d4e3c40b1a0a603
last_modified_at: 2024-10-27
related_topics:
  - title: English version
    url: /en/common/crane-index-filter.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/crane-index-filter.html
    icon: bi bi-globe
tldri18n_status: 2
---
# crane index filter

Wijzigt een remote index door te filteren op basis van platform.
Meer informatie: <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_index_filter.md>.

- Wijzig de remote index:

`crane index filter`

- Specificeer het platform(en) dat je wilt behouden uit de basis in de vorm os/arch`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/variant</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">:osversion</span><span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,<platform></span>`:

`crane index filter --platform `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">platform1 platform2 ...</span>

- Tag die toegepast moet worden op de resulterende image:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--tags</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag_naam</span>

- Toon help:

`crane index filter `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
