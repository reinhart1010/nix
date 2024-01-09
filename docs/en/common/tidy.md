---
layout: page
title: common/tidy (English)
description: "Clean up and pretty print HTML, XHTML and XML files."
content_hash: 2e3280e642eb0adb13508e25726e5f85d8ad1ddc
last_modified_at: 2024-01-09
tldri18n_status: 2
---
# tidy

Clean up and pretty print HTML, XHTML and XML files.
NOTE: `tidy` cannot preserve original indentation.
More information: <https://api.html-tidy.org/tidy/tidylib_api_5.2.0/tidy_cmd.html>.

- Pretty print an HTML file:

`tidy `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>

- Enable [i]ndentation, [w]rapping lines in 100, saving to `output.html`:

`tidy --indent y --wrap 100 -output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output.html</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>

- Modify an HTML file in-place using a configuration file:

`tidy -config `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/configuration</span>` -modify `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file.html</span>
