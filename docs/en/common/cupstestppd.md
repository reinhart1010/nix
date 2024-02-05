---
layout: page
title: common/cupstestppd (English)
description: "Test conformance of PPD files to the version 4.3 of the specification."
content_hash: a564472c90fd083730030e8d3e02294efba5032e
last_modified_at: 2024-02-05
tldri18n_status: 2
---
# cupstestppd

Test conformance of PPD files to the version 4.3 of the specification.
Error codes (1, 2, 3 and 4, respectively): bad CLI arguments, unable to open file, unskippable format errors and non-conformance with PPD specification.
Note: this command is deprecated.
See also: `lpadmin`.
More information: <https://openprinting.github.io/cups/doc/man-cupstestppd.html>.

- Test the conformance of one or more files in quiet mode:

`cupstestppd -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.ppd path/to/file2.ppd ...</span>

- Get the PPD file from `stdin`, showing detailed conformance testing results:

`cupstestppd -v - < `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.ppd</span>

- Test all PPD files under the current directory, printing the names of each file that does not conform:

`find . -name \*.ppd \! -execdir cupstestppd -q '{}' \; -print`
