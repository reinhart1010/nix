---
layout: page
title: common/convmv (English)
description: "Convert filenames (NOT file content) from one encoding to another."
content_hash: 1e2f2cd2f819179bef3fc9bd1437c7b8a138d8f2
related_topics:
  - title: italiano version
    url: /it/common/convmv.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/convmv.html
    icon: bi bi-globe
---
# convmv

Convert filenames (NOT file content) from one encoding to another.
More information: <https://www.j3e.de/linux/convmv/man/>.

- Test filename encoding conversion (don't actually change the filename):

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>

- Convert filename encoding and rename the file to the new encoding:

`convmv -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">from_encoding</span>` -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">to_encoding</span>` --notest `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file</span>
