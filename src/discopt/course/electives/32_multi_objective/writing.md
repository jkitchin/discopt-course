# Writing assignment — Lesson 32

A plant manager asks you for "the optimal facility plan" when both cost and
CO₂ emissions matter. In about 700 words, explain why you will hand back a
Pareto front rather than a single answer, and how you would help the manager
choose a plan from it. Address:

1. **Why weighted sums are not enough.** Explain supported and unsupported
   efficient points. Use a figure or numbers from Exercise 3 or 5 to show a
   point that no choice of weights recovers {cite:p}`ehrgott-2005`.
2. **What the ε-constraint multiplier means.** Interpret the multiplier of the
   emissions row as a marginal abatement cost, using your values from
   Exercise 2. State when this interpretation breaks down (kinks, integer
   variables) {cite:p}`miettinen-1999`.
3. **How complete and honest your front is.** Discuss grid resolution,
   weakly efficient anchors and the `incomplete` flag, and which indicator
   (hypervolume, IGD, spread) you would report to show that your front is
   good {cite:p}`zitzler-deb-thiele-2000`.
4. **Choosing a compromise.** Compare at least two selection rules (for
   example, distance to the ideal and a carbon-price threshold). Explain why
   the final choice belongs to the decision maker, not the solver
   {cite:p}`marler-arora-2004`.
