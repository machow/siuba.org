# Function reference


## Core verbs - one table

| | |
| --- | --- |
| [arrange][siuba.arrange] | Sort rows based on one or more columns. |
| [count][siuba.count] | Count observations by group. |
| [distinct][siuba.distinct] | Count observations by group. |
| [filter][siuba.filter] | Keep rows that match condition. |
| [head][siuba.head] | Keep the first n rows of data. |
| [mutate][siuba.mutate], [transmute][siuba.transmute] | Create or replace columns. |
| [rename][siuba.rename] | Rename columns. |
| [select][siuba.select] | Keep, drop, or rename specific columns. |
| [summarize][siuba.summarize] | Calculate a single number per grouping. |
| [group_by][siuba.group_by], [ungroup][siuba.ungroup] | Specify groups for splitting rows of data. |

## Core verbs - two table

| | |
| --- | --- |
| [inner_join, left_join, right_join, full_join][siuba.join] | Mutating joins |
| [semi_join][siuba.semi_join], [anti_join][siuba.anti_join] | Filtering joins |

## Query verbs

| | |
| --- | --- |
| [collect][siuba.collect] | Retrieve data into a DataFrame. |
| [show_query][siuba.show_query] | Print the query being generated. |

## Tidy verbs

| | |
| --- | --- |
| [complete][siuba.complete] | Add rows for missing combinations in the data. |
| [extract][siuba.extract] | Add new columns by matching a pattern on a column of strings. |
| [gather][siuba.gather], [spread][siuba.spread] | Gather columns in to long format. Spread out to wide format. |
| [pivot_longer][siuba.experimental.pivot.pivot_longer], [pivot_wider][siuba.experimental.pivot.pivot_wider] | Change rows of data to columns, or columns to rows. More comprehensive than spread and gather. |
| [separate][siuba.separate], [unite][siuba.unite] | Add new columns by splitting a character column. |
| [nest][siuba.nest], [unnest][siuba.unnest] | Create a column where each entry is a DataFrame. |

## Column Operations

### Forcats

| | |
| --- | --- |
| [fct_collapse][siuba.dply.forcats.fct_collapse] | Rename categories. Optionally group all others. |
| [fct_infreq][siuba.dply.forcats.fct_infreq] | Order categories by frequency (largest first) |
| [fct_inorder][siuba.dply.forcats.fct_inorder] | Order categories by when they first appear. |
| [fct_lump][siuba.dply.forcats.fct_lump] | Lump infrequently observed categories together. |
| [fct_recode][siuba.dply.forcats.fct_recode] | Rename categories. |
| [fct_reorder][siuba.dply.forcats.fct_reorder] | Reordered categories, using a calculation over another column. |
| [fct_rev][siuba.dply.forcats.fct_rev] | Reverse category levels. |

### Datetime

| | |
| --- | --- |
| [floor_date, ceil_date][siuba.experimental.datetime.floor_date] | Round datetimes down or up to a specific granularity (e.g. week). |

### Vector

| | |
| --- | --- |
| [between()][siuba.dply.vector.between] | Check whether values are in a specified range. |
| [case_when()][siuba.case_when], [if_else()][siuba.if_else] | Generalized if statements. |
| [coalesce()][siuba.dply.vector.coalesce] | Use first non-missing element across columns. |
| [cumall()][siuba.dply.vector.cumall], [cumany()][siuba.dply.vector.cumany], [cummean()][siuba.dply.vector.cummean] | Cumulative all, any, and mean. |
| [lag()][siuba.dply.vector.lag], [lead()][siuba.dply.vector.lead] | Shift values later (lag) or earlier (lead) in time. |
| [n()][siuba.dply.vector.n] | Calculate the number of observations in a vector. |
| [n_distinct()][siuba.dply.vector.n_distinct] | Count the number of unique values. |
| [na_if()][siuba.dply.vector.na_if] | Convert a value to NA. |
| [near()][siuba.dply.vector.near] | Check whether every pair of values in two vectors are close. |
| [nth()][siuba.dply.vector.nth], [first()][siuba.dply.vector.first], [last()][siuba.dply.vector.last] | Return the first, last, or nth value. |
| [row_number()][siuba.dply.vector.row_number], [ntile()][siuba.dply.vector.ntile], [min_rank()][siuba.dply.vector.min_rank], [dense_rank()][siuba.dply.vector.dense_rank], [percent_rank()][siuba.dply.vector.percent_rank], [cume_dist()][siuba.dply.vector.cume_dist] | Windowed rank functions. |
