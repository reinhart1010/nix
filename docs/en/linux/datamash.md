---
layout: page
title: linux/datamash (English)
description: "Perform basic numeric, textual and statistical operations on input textual data files."
content_hash: 99f3b7875f6ff1ac4025533de2baf6029b10e9ea
last_modified_at: 2024-10-12
tldri18n_status: 2
---
# datamash

Perform basic numeric, textual and statistical operations on input textual data files.
More information: <https://www.gnu.org/software/datamash/>.

- Get max, min, mean and median of a single column of numbers:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- Get the mean of a single column of float numbers (floats must use "," and not "."):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- Get the mean of a single column of numbers with a given decimal precision:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_decimals_wanted</span>` mean 1`

- Get the mean of a single column of numbers ignoring "Na" and "NaN" (literal) strings:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
