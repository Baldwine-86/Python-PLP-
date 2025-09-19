# Part 4: Streamlit App (code only, run separately)

import streamlit as st

st.title("CORD-19 Data Explorer")
st.write("Exploring COVID-19 research papers interactively")

# Filter by year range
year_range = st.slider("Select year range", 2015, 2025, (2019, 2021))
filtered = df[df['year'].between(year_range[0], year_range[1])]

# Publications by year
year_counts = filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color="skyblue")
ax.set_title("Publications by Year")
st.pyplot(fig)

# Show top journals
st.write("Top Journals", filtered['journal'].value_counts().head(10))

# Sample data
st.write(filtered[['title', 'authors', 'journal', 'year']].head(20))
