---
layout: page
title: linux/datamash (English)
description: "Tool to perform basic numeric, textual and statistical operations on input textual data files."
content_hash: 10f3e9ba63e808bad260a1ae48a16e81a349d66c
---
# datamash

Tool to perform basic numeric, textual and statistical operations on input textual data files.
More information: <http://www.gnu.org/software/datamash/>.

- Get max, min, mean and median of a single column of numbers:

`seq 3 | datamash max 1 min 1 mean 1 median 1`

- Get the mean of a single column of float numbers (floats must use "," and not "."):

`echo -e '1.0\n2.5\n3.1\n4.3\n5.6\n5.7' | tr '.' ',' | datamash mean 1`

- Get the mean of a single column of numbers with a given decimal precision:

`echo -e '1\n2\n3\n4\n5\n5' | datamash -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">number_of_decimals_wanted</span>` mean 1`

- Get the mean of a single column of numbers ignoring "Na" and "NaN" (literal) strings:

`echo -e '1\n2\nNa\n3\nNaN' | datamash --narm mean 1`
