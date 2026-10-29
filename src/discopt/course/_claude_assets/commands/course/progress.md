---
description: Show the student's discopt-course progress
---

Show the student's progress through the course.

1. If `course/progress.yaml` does not exist (`discopt tutor install`
   normally seeds it), copy `course/progress.template.yaml` to
   `course/progress.yaml` (using the `cp` command via Bash) and tell the
   student you've initialized it.
2. Read `course/progress.yaml`.
3. Render a table:

   ```
   Track          Lessons completed     Avg score    Next
   --------------------------------------------------------
   basic          7 / 10                82           basic/08_unconstrained_nlp
   intermediate   0 / 10                -            (locked - finish basic first)
   advanced       0 / 10                -            (locked)
   electives      0 / 3                 -            (31 after intermediate, 32-33 after basic)
   ```

4. Highlight any lessons below the 70-point threshold and recommend
   revising those first.
5. Show the lesson the student should attempt next.

A track is "unlocked" if the student has completed (≥70 on every lesson) the
prior track. Lessons within a track unlock in order. Electives are optional
and unlock individually: 31 (dynamic optimization) after the intermediate
track, 32 (multi-objective) and 33 (piecewise-linear and grey-box models)
after the basic track. They never block
progress through the core tracks.
