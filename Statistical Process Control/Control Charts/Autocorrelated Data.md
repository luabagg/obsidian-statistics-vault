---
dg-publish: true
aliases:
  - Control Charts for Autocorrelated Data
  - Autocorrelated Data in SPC
---

# Control Charts for Autocorrelated Data

Autocorrelated process data can break ordinary Shewhart interpretation.
Nearby observations are not independent.
Time-series methods account for internal structure such as autocorrelation, trend, or seasonality.[^nist-time-series]

## Prerequisites

Prerequisites: I-MR charts and basic time-series autocorrelation.

## Process Context

Autocorrelation is common in continuous chemical processes, sensor streams, temperature profiles, financial operations, and automated measurements sampled faster than the process can physically change.

## Definition

For an autocorrelated series $y_t$, a robust SPC approach models the predictable structure first and charts residuals:

$$
e_t = y_t - \hat{y}_{t|t-1}.
$$

The residual chart asks whether the unexplained part of the process changed.

## Assumptions / Requirements

- Observations are time ordered and equally spaced, or the model explicitly handles spacing.
- Autocorrelation is diagnosed before ordinary control limits are trusted.
- The residual model is validated; residuals should be approximately stable and uncorrelated.
- Process knowledge supports the model and sampling interval.

## Control Limits / Formula

For residuals with mean near zero and estimated residual standard deviation $\hat{\sigma}_e$:

$$
UCL_e = 3\hat{\sigma}_e,\qquad CL_e=0,\qquad LCL_e=-3\hat{\sigma}_e.
$$

This residual chart formula is not universal for all autocorrelated processes.

## Interpretation Rules

- A naive I-MR chart may false alarm or miss shifts when autocorrelation is strong.
- Chart the residuals only after the time-series model is checked.
- A residual signal means the process deviated from its expected dynamic behavior.
- Trends and seasonality should be modeled or removed before Shewhart-style limits are interpreted.

## Worked Example

One furnace temperature series follows the forecast $\hat{y}_{t|t-1}=0.8y_{t-1}+20$.
If one observation is $y_{t-1}=100$, the forecast is $100$.
If the next observed value is $104$, the residual is $e_t=4$.
With $\hat{\sigma}_e=1.2$, the residual UCL is $3.6$, so this residual is a signal.

## Common Mistakes

- Applying I-MR limits to highly autocorrelated sensor data without diagnosis.
- Treating residual charting as valid without checking residual autocorrelation.
- Sampling too frequently and then blaming the chart for false alarms.
- Removing trend without preserving the operational meaning of the signal.

## Connections

| Related note | Use |
|---|---|
| [[I-MR Chart|I-MR / X-MR chart]] | Baseline individuals chart |
| [[Control Charts|Control charts]] | Chart selection |
| [[Common-Cause and Special-Cause Variation]] | Signal interpretation |
| [[Control Limits and Specification Limits]] | Limit distinction |

## References

[^nist-time-series]: NIST/SEMATECH, *e-Handbook of Statistical Methods*, "Introduction to Time Series Analysis", https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm
