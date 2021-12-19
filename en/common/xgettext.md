---
layout: page
title: common/xgettext (English)
description: "Extract gettext strings from code files."
content_hash: 5e0bfe42182226c8258e123f62e1828fba729abd
---
# xgettext

Extract gettext strings from code files.
More information: <https://www.gnu.org/software/gettext/manual/html_node/xgettext-Invocation.html>.

- Scan file and output strings to `messages.po`:

`xgettext `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Use a different output filename:

`xgettext --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Append new strings to an existing file:

`xgettext --join-existing --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>

- Don't add a header containing metadata to the output file:

`xgettext --omit-header `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/input_file</span>
