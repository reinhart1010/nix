---
layout: page
title: common/pdfseparate (English)
description: "Portable Document Format (PDF) file page extractor."
content_hash: dceb9f1d5c5b180e72e899e4a61add219ece80ef
---
# pdfseparate

Portable Document Format (PDF) file page extractor.
More information: <https://manpages.debian.org/unstable/poppler-utils/pdfseparate.1.en.html>.

- Extract pages from PDF file and make a separate PDF file for each page:

`pdfseparate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>

- Specify the first/start page for extraction:

`pdfseparate -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>

- Specify the last page for extraction:

`pdfseparate -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">10</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/source_filename.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/destination_filename-%d.pdf</span>
