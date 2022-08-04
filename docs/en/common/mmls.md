---
layout: page
title: common/mmls (English)
description: "Display the partition layout of a volume system."
content_hash: f4633f9cb3e2c1e64646b35e44e11ffeb7172a97
---
# mmls

Display the partition layout of a volume system.
More information: <https://wiki.sleuthkit.org/index.php?title=Mmls>.

- Display the partition table stored in an image file:

`mmls `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Display the partition table with an additional column for the partition size:

`mmls -B -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>

- Display the partition table in a split EWF image:

`mmls -i ewf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.e01</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">image.e02</span>

- Display nested partition tables:

`mmls -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nested_table_type</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">offset</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">path/to/image_file</span>
