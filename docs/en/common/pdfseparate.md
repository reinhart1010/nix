---
layout: page
title: common/pdfseparate (English)
description: "Portable Document Format (PDF) file page extractor."
content_hash: 21caf5e1944d5a6efda393355b3c81e2441da57a
last_modified_at: 2023-05-14
related_topics:
  - title: Deutsch version
    url: /de/common/pdfseparate.html
    icon: bi bi-globe
---
# pdfseparate

Portable Document Format (PDF) file page extractor.
More information: <https://manpages.debian.org/latest/poppler-utils/pdfseparate.1.en.html>.

- Extract pages from PDF file and make a separate PDF file for each page:

`pdfseparate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>

- Specify the first/start page for extraction:

`pdfseparate -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>

- Specify the last page for extraction:

`pdfseparate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>
