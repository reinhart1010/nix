---
layout: page
title: common/ufraw-batch (English)
description: "Convert RAW files from cameras into standard image files."
content_hash: 2bfedc0ec73250134cd8b410422510f21abae4bf
last_modified_at: 2024-03-14
tldri18n_status: 2
---
# ufraw-batch

Convert RAW files from cameras into standard image files.
More information: <https://manned.org/ufraw-batch>.

- Simply convert RAW files to JPEG:

`ufraw-batch --out-type=jpg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Simply convert RAW files to PNG:

`ufraw-batch --out-type=png `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Extract the preview image from the raw file:

`ufraw-batch --embedded-image `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>

- Save the file with size up to the given maximums MAX1 and MAX2:

`ufraw-batch --size=MAX1,MAX2 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">input_file(s)</span>
