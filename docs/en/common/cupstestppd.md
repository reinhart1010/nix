---
layout: page
title: common/cupstestppd (English)
description: "Test conformance of PPD files to the version 4.3 of the specification."
content_hash: 98b4c7941295c5628ab2ad43155a29848ba2e6b7
last_modified_at: 2023-12-29
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/cupstestppd.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># cupstestppd

Test conformance of PPD files to the version 4.3 of the specification.
Error codes (1, 2, 3 and 4, respectively): bad CLI arguments, unable to open file, unskippable format errors and non-conformance with PPD specification.
NOTE: this command is deprecated.
See also: `lpadmin`.
More information: <https://openprinting.github.io/cups/doc/man-cupstestppd.html>.

- Test the conformance of one or more files in quiet mode:

`cupstestppd -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.ppd path/to/file2.ppd ...</span>

- Get the PPD file from `stdin`, showing detailed conformance testing results:

`cupstestppd -v - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppd</span>

- Test all PPD files under the current directory, printing the names of each file that does not conform:

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`
