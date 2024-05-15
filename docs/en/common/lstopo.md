---
layout: page
title: common/lstopo (English)
description: "Show the hardware topology of the system."
content_hash: 9064e92bbf2ec002081b2ae9940004544ad69f29
last_modified_at: 2024-05-15
tldri18n_status: 2
---
# lstopo

Show the hardware topology of the system.
More information: <https://manned.org/lstopo>.

- Show the summarized system topology in a graphical window (or print to console if no graphical display is available):

`lstopo`

- Show the full system topology without summarizations:

`lstopo --no-factorize`

- Show the summarized system topology with only [p]hysical indices (i.e. as seen by the OS):

`lstopo --physical`

- Write the full system topology to a file in the specified format:

`lstopo --no-factorize --output-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">console|ascii|tex|fig|svg|pdf|ps|png|xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/file</span>

- Output in monochrome or greyscale:

`lstopo --palette `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|grey</span>
