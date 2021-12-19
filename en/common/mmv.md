---
layout: page
title: common/mmv (English)
description: "Move and rename files in bulk."
content_hash: 87d61154068e001edc77bcc35e9d5e8b9d9210a4
---
# mmv

Move and rename files in bulk.
More information: <https://manned.org/mmv.1>.

- Rename all files with a certain extension to a different extension:

`mmv "*`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.old_extension</span>`" "#1`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.new_extension</span>`"`

- Copy `report6part4.txt` to `./french/rapport6partie4.txt` along with all similarly named files:

`mmv -c "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">report*part*.txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./french/rapport#1partie#2.txt</span>`"`

- Append all `.txt` files into one file:

`mmv -a "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">*.txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">all.txt</span>`"`

- Convert dates in filenames from "M-D-Y" format to "D-M-Y" format:

`mmv "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[0-1][0-9]-[0-3][0-9]-[0-9][0-9][0-9][0-9].txt</span>`" "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">#3#4-#1#2-#5#6#7#8.txt</span>`"`
