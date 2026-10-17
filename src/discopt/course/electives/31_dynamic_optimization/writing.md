# Writing assignment — Lesson 31

In ~600 words, advise a process engineer who has an ODE model and a
simulator, and who plans to optimize a batch recipe by wrapping the
simulator inside an optimizer (single shooting). Compare that sequential
approach with the simultaneous (collocation) approach used in this lesson.
Use {cite:p}`Biegler2010,Cuthrell1987`; {cite:p}`Betts2010` is
recommended. Address:
(i) what the NLP looks like in each approach (variables, constraints,
sparsity) and why the simultaneous approach copes better with unstable
dynamics and state path constraints;
(ii) the two kinds of error in a transcribed solution (state
discretization and control parametrization), illustrated with numbers
from your Exercise 3 or 5 table, and how you would choose the number of
finite elements and collocation points;
(iii) why a `"feasible"` (local, uncertified) status is the honest
outcome for most dynamic optimization problems, and what you would do to
gain confidence in the answer (validation by simulation, multiple starts,
grid refinement).
