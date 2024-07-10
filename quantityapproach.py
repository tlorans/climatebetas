import streamlit as st 
import numpy as np
import plotly.graph_objs as go
import numpy as np


st.title("Quantity-Based Approach")

st.write(r"""
The idea here, exposed by Alekseev et al. (2022), is to exploit changes from 
individual portfolio holdings to estimate climate betas.
         
Going back to the optimal portfolio of investor $i$ in PST (2021), we have:
         """)

st.latex(r"""

\begin{equation}
    X_i = \frac{1}{a}\Sigma^{-1} ( \mu - c_i \sigma_{\tilde{\epsilon}_1, \tilde{C}_1})
\end{equation}
""")

st.write(r"""
The investor $i$ may be affected by an idiocyncratic shock that may change
his perception of climate risks $c_i$. We can then estimate the climate betas
as the change in the optimal portfolio weights following the change in perception
of climate risks.
         """)


# Function to calculate the optimal portfolio
def optimal_portfolio(a, c_i, mu, Sigma, sigma_epsilon_C1):
    Sigma_inv = np.linalg.inv(Sigma)
    X_i = (1 / a) * Sigma_inv.dot(mu - c_i * sigma_epsilon_C1)
    # Normalize the weights to sum up to 1
    X_i = X_i / np.sum(X_i)
    return X_i

# Define specific parameters for 5 assets
num_assets = 5
mu = np.array([0.12, 0.10, 0.08, 0.11, 0.09])  # Expected returns
Sigma = np.array([
    [0.1, 0.01, 0.02, 0.01, 0.02],
    [0.01, 0.1, 0.01, 0.02, 0.01],
    [0.02, 0.01, 0.1, 0.01, 0.02],
    [0.01, 0.02, 0.01, 0.1, 0.01],
    [0.02, 0.01, 0.02, 0.01, 0.1]
])  # Covariance matrix
sigma_epsilon_C1 = np.array([-0.8, 0.9, -0.6, 0.7, -0.4])  # Covariance with climate risk

a = 2  # Risk aversion coefficient

# Interactive slider for c_i
c_i = 0.5
delta_c_i = st.sidebar.slider("Change in Climate Risk Perception (Δ$c_i$)", 0., 1.0, 0.1, 0.01)

# Calculate the optimal portfolio for the initial c_i
X_i_initial = optimal_portfolio(a, c_i, mu, Sigma, sigma_epsilon_C1)
# Calculate the optimal portfolio for the changed c_i
X_i_changed = optimal_portfolio(a, c_i + delta_c_i, mu, Sigma, sigma_epsilon_C1)

# Estimate climate betas as the change in the optimal portfolio weights
climate_betas = X_i_changed - X_i_initial

# Plot the portfolio weights using Plotly
fig = go.Figure()

# Plot initial portfolio weights
fig.add_trace(go.Scatter(
    x=np.arange(num_assets),
    y=X_i_initial,
    mode='lines+markers',
    name='Initial Portfolio Weights',
    marker=dict(size=10, color='blue', opacity=0.6)
))

# Plot changed portfolio weights
fig.add_trace(go.Scatter(
    x=np.arange(num_assets),
    y=X_i_changed,
    mode='lines+markers',
    name=f'Portfolio Weights after Change in $c_i$',
    marker=dict(size=10, color='red', opacity=0.6)
))

# Plot climate betas
fig.add_trace(go.Bar(
    x=np.arange(num_assets),
    y=climate_betas,
    name='Estimated Climate Betas',
    marker=dict(color='green', opacity=0.6)
))

fig.update_layout(
    title=f'Portfolio Weights and Estimated Climate Betas',
    xaxis_title='Asset',
    yaxis_title='Weight / Beta',
    legend_title="Legend",
    template='plotly_white'
)

# Display the plot in Streamlit
st.plotly_chart(fig)
