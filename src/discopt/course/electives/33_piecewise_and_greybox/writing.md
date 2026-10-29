# Writing assignment — Lesson 33

Your team's process model has grown three kinds of parts: a pump curve and an
electricity tariff that arrive as tables, a few nonlinear rate laws written as
formulas, and a vendor's reactor simulator that returns values and derivatives
but no equations. A colleague proposes to "just approximate everything
piecewise-linearly and call a MILP solver". In about 700 words, write the memo
that explains what each part should become and what the final answer will and
will not certify. Address:

1. **Tables are exact, approximations are not.** Explain why `m.piecewise`
   on a datasheet table gives a certified optimum of the declared model, while
   tabulating a formula does not, unless the approximation is an outer one.
   Use the $\sqrt{x}$ example of Reading §3 or your own numbers from
   Exercise 3 {cite:p}`Vielma2010`.
2. **Choosing an encoding.** Compare the sizes and LP strength of the four
   encodings, using your counts from Exercise 1, and recommend one for a long
   table in a model that must be exported {cite:p}`Vielma2011`.
3. **What a grey box costs.** Explain why a block that can only be evaluated
   admits no convex relaxation, so a model containing it can be at best
   `feasible`, and why `discopt` refuses it alongside integer variables. Use
   the local-optimum trap of Reading §5 or your Exercise 4 results
   {cite:p}`Biegler2010`.
4. **A plan for the mixed model.** Using Exercise 5, propose how to handle a
   model that needs both a table (binaries) and a grey box: a symbolic twin,
   enumeration of the discrete choices, or a trust-region surrogate method.
   State exactly what each option proves {cite:p}`Eason2016`.
