import streamlit as st 
import numpy as np
import plotly.graph_objs as go
import numpy as np


st.title("Narrative Approach")


st.write(r"""
In PST (2021), the assumption is that 
some characteristics
of stocks, approximated with 
environmental scores in Pastor *et al.* (2022)) $g_n$,
may be negatively correlated with $\psi_n$. 
For example, in the case of transition risks,
"greener" firms may have negative $\psi_n$,
while "browner" firms may have positive $\psi_n$.
In that case, with $\zeta > 0$, we have:
""")


# Slider for zeta
zeta = st.sidebar.slider('Select a value for zeta', min_value=-1., max_value=1., value=1.0, step=0.1)
c_bar = st.sidebar.slider('Select a value for c_bar', min_value=0., max_value=10.0, value=1.0, step=0.1)


st.latex(r"""
\begin{equation}
    \psi_n = -\zeta g_n
\end{equation}
""")


# Generate sample data
g_n = np.linspace(-1, 1, 100)
mu_m = 1.0
beta_m = 0
rho_mC_squared = 0.5

# Calculate the variables
psi_n = -zeta * g_n
alpha_n = - c_bar * (1 - rho_mC_squared) * zeta * g_n
alpha_n_benchmark = - 0 * (1 - rho_mC_squared) * zeta * g_n

# Create scatter plot between psi_n and g_n
fig1 = go.Figure()
fig1.add_trace(go.Scatter(x=g_n, y=psi_n, mode='lines', name='psi_n'))
fig1.update_layout(
    title="Scatter Plot between psi_n and g_n",
    xaxis_title="Environmental Score (g_n)",
    yaxis_title="psi_n",
    legend_title="Variables"
)

st.plotly_chart(fig1)


st.write(r"""
and therefore:
""")

st.latex(r"""

\begin{equation}
    \mu = \mu_m \beta_m - \bar{c}(1 - \rho^2_{mC}) \zeta g
\end{equation}
""")

st.write(r"""
and:
""")

st.latex(r"""
\begin{equation}
    \alpha_n = - \bar{c}(1 - \rho^2_{mC}) \zeta g_n
\end{equation}
""")

st.write(r"""
The climate risks hedging portfolio will 
therefore be proportional to the climate risks-related 
characteristics
of the stocks $g$.
""")


# Create plot for alpha_n and g_n
fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=g_n, y=alpha_n, mode='lines', name='alpha_n'))
fig2.add_trace(go.Scatter(x=g_n, y=alpha_n_benchmark, mode='lines', name='alpha_n (c_bar = 0)', line=dict(dash='dash')))
fig2.update_layout(
    title="Relationship between alpha_n and g_n",
    xaxis_title="Environmental Score (g_n)",
    yaxis_title="alpha_n",
    legend_title="Variables"
)

# Display the plots in Streamlit
st.plotly_chart(fig2)
