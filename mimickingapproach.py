import streamlit as st 
import numpy as np
import plotly.graph_objs as go
import numpy as np


st.title("Mimicking Approach")

st.write(r"""
Another approach is mimicking portfolio from Lamont (2001) [1],
as advocated by Engle *et al.* (2020) [2]. 
We may not observe $\tilde{C}_1$ directly, and 
therefore estimate $\psi_n$ by regressing the unexpected returns
$\tilde{\epsilon}_1$ on the climate risks $\tilde{C}_1$. 
         
But we can observe the change in perception of climate risks 
($\bar{c}_1 - E_0(\bar{c}_1)$) by taking unexpected change of climate concerns 
from news articles, as in Pastor *et al.* (2022). 

We can therefore estimate $\psi_n$ by regressing unexpected returns
$\tilde{\epsilon}_1$ on the change in perception of climate risks 
($\bar{c}_1 - E_0(\bar{c}_1)$).
""")

# Slider for psi_n
psi_n = st.slider('Select a value for psi_n (slope of regression line)', min_value=-2.0, max_value=2.0, value=0.5, step=0.1)

# Generate sample data
np.random.seed(42)
climate_risk_perception_change = np.random.normal(0, 1, 100)
unexpected_returns = psi_n * climate_risk_perception_change + np.random.normal(0, 0.5, 100)

# Create scatter plot with regression line
fig = go.Figure()

# Add scatter plot for data points
fig.add_trace(go.Scatter(x=climate_risk_perception_change, y=unexpected_returns, mode='markers', name='Data Points'))

# Add regression line
x_vals = np.array([-3, 3])
y_vals = psi_n * x_vals
fig.add_trace(go.Scatter(x=x_vals, y=y_vals, mode='lines', name='Regression Line', line=dict(color='red')))

# Update layout
fig.update_layout(
    title="Unexpected Returns vs. Change in Climate Risk Perception",
    xaxis_title="Change in Climate Risk Perception (Δc)",
    yaxis_title="Unexpected Returns (ε)",
    legend_title="Legend"
)

# Display the plot in Streamlit
st.plotly_chart(fig)

st.markdown("""

## References
            
[1]: Lamont, O. A. (2001). Economic tracking portfolios. Journal of Econometrics, 105(1), 161-184.
            
[2]: Engle, R. F., Giglio, S., Kelly, B., Lee, H., & Stroebel, J. (2020). Hedging climate change news. The Review of Financial Studies, 33(3), 1184-1216.
            
            """)