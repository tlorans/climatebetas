import streamlit as st

intro_page = st.Page("intro.py", title = "Introduction")
narrative_page = st.Page("narrativeapproach.py", title = "Narrative Approach")
mimicking_page = st.Page("mimickingapproach.py", title = "Mimicking Approach")
quantity_page = st.Page("quantityapproach.py", title = "Quantity-Based Approach")

pg = st.navigation([intro_page,
                     narrative_page,
                    mimicking_page,
                    quantity_page
                    ])
st.set_page_config(page_title="Climate Betas")
pg.run()