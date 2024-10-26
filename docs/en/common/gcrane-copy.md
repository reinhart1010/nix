---
layout: page
title: common/gcrane-copy (English)
description: "Efficiently copy a remote image from source to target while retaining the digest value."
content_hash: 08ab9751b9796cbe5b08eec6440d304f257b3ae1
last_modified_at: 2024-10-26
related_topics:
  - title: 한국어 version
    url: /ko/common/gcrane-copy.html
    icon: bi bi-globe
tldri18n_status: 2
---
# gcrane copy

Efficiently copy a remote image from source to target while retaining the digest value.
More information: <https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md>.

- Copy an image from source to target:

`gcrane `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">cp|copy</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>

- Set the maximum number of concurrent copies, defaults to 20:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-j|--jobs</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nr_of_copies</span>

- Whether to recurse through repositories:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">target</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-r|--recursive</span>

- Display help:

`gcrane copy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-h|--help</span>
