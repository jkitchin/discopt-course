---
description: Verify that all citations in course readings resolve in course/references.bib
---

Verify that every `{cite:p}` and `{cite:t}` key used anywhere under
`course/` (including the student's `writing_response.md` files) exists in
`course/references.bib`.

The course bibliography is `course/references.bib` (it ships with
discopt-course and `discopt tutor install` copies it into `course/`).
Lesson files that say `docs/references.bib` mean this file; in a
discopt-course repo checkout it lives at `src/discopt/course/references.bib`.

Procedure:

1. Use Bash + grep to extract every citation key from
   `course/**/*.ipynb` and `course/**/*.md`. Pattern: `{cite:[pt]}`
   followed by a backticked `<key>` or `<key1>,<key2>`. Ignore prose that
   merely mentions the role (e.g. "`{cite:p}` keys resolve in ...").
2. Use Bash + grep to extract every `@type{key,` from
   `course/references.bib`.
3. Diff the two sets. Report any keys cited but not defined.
4. (Optional) For each course-cited key, fetch its DOI/URL via WebFetch to
   verify the citation refers to a real published work — highlight any keys
   that look fabricated.

Print a summary table:

```
Cited keys: 47
Defined in references.bib: 47
Missing: 0
Suspicious (no DOI/URL on file): 2  (Foo2099, Bar1900)
```

Exit with a non-zero status (in the conceptual sense — say "FAIL") if any
keys are cited but undefined.
