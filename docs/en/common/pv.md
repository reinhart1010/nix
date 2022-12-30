---
layout: page
title: common/pv (English)
description: "Monitor the progress of data through a pipe."
content_hash: e5b11326d163f76a2e19fa70062874c4ce98331c
last_modified_at: 2022-12-30
---
# pv

Monitor the progress of data through a pipe.
More information: <https://manned.org/pv>.

- Print the contents of the file and display a progress bar:

`pv `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Measure the speed and amount of data flow between pipes (`--size` is optional):

`command1 | pv --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expected_amount_of_data_for_eta</span>` | command2`

- Filter a file, see both progress and amount of output data:

`pv -cN in `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">big_text_file</span>` | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pattern</span>` | pv -cN out > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">filtered_file</span>

- Attach to an already running process and see its file reading progress:

`pv -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">PID</span>

- Read an erroneous file, skip errors as `dd conv=sync,noerror` would:

`pv -EE `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/faulty_media</span>` > image.img`

- Stop reading after reading specified amount of data, rate limit to 1K/s:

`pv -L 1K --stop-at --size `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">maximum_file_size_to_be_read</span>
