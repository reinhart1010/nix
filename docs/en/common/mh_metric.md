---
layout: page
title: common/mh_metric (English)
description: "Calculate and enforce code metrics for MATLAB or Octave code."
content_hash: 621c8bfda5cbb2be4cc438925fde3b2f1b23f766
last_modified_at: 2023-11-12
tldri18n_status: 2
---
# mh_metric

Calculate and enforce code metrics for MATLAB or Octave code.
More information: <https://misshit.org>.

- Print the code metrics for the specified files:

`mh_metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.m path/to/file2.m ...</span>

- Print the code metrics for the specified Octave files:

`mh_metric --octave `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file1.m path/to/file2.m ...</span>

- Print the code metrics for the specified directory recursively:

`mh_metric `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/directory</span>

- Print the code metrics for the current directory:

`mh_metric`

- Print the code metrics report in HTML or JSON format:

`mh_metric --`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">html|json</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/output_file</span>
