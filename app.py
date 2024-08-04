import streamlit as st
import requests
import json

# Function to fetch data from the API
def fetch_data(query):
    url = "https://google.serper.dev/search"
    payload = json.dumps({
      "q": query,
      "gl": "de"
    })
    headers = {
      'X-API-KEY': '72961141ec55e220e7bfac56098cc1627f49bd9b',
      'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=payload)
    return response.json()

# List of companies to display
companies = [
    "Mineraloelraffinerie Oberrhein GmbH & Co. KG",
    "Bayernoil Raffineriegesellschaft mbH",
    "PCK Raffinerie GmbH",
    "Shell Deutschland Oil GmbH Rheinland Raffinerie",
    "Salzgitter Flachstahl GmbH"
]

# Display the list of companies
st.title("Company Information")
selected_company = st.selectbox("Select a Company", companies)

if selected_company:
    # Fetch and display data for the selected company
    data = fetch_data(selected_company)

    # Display data using Streamlit
    st.header("Company Information")
    
    # Knowledge Graph Section
    st.header("Knowledge Graph")
    knowledge_graph = data.get("knowledgeGraph", {})
    if knowledge_graph:
        st.subheader(knowledge_graph.get("title", "N/A"))
        st.write(f"**Type:** {knowledge_graph.get('type', 'N/A')}")
        st.write(f"**Website:** [Link]({knowledge_graph.get('website', '#')})")
        st.write(f"**Rating:** {knowledge_graph.get('rating', 'N/A')} (Based on {knowledge_graph.get('ratingCount', 'N/A')} reviews)")
        st.image(knowledge_graph.get("imageUrl", "https://via.placeholder.com/150"))

        # Display attributes
        st.write("**Attributes:**")
        attributes = knowledge_graph.get("attributes", {})
        for key, value in attributes.items():
            st.write(f"**{key}:** {value}")

    # Organic Results Section
    st.header("Search Results")
    for result in data.get("organic", []):
        st.subheader(result.get("title", "N/A"))
        st.write(result.get("snippet", "N/A"))
        st.write(f"[Read more]({result.get('link', '#')})")

    # People Also Ask Section
    st.header("People Also Ask")
    for question in data.get("peopleAlsoAsk", []):
        st.subheader(question.get("question", "N/A"))
        st.write(question.get("snippet", "N/A"))
        st.write(f"[Read more]({question.get('link', '#')})")

    # Related Searches Section
    st.header("Related Searches")
    for search in data.get("relatedSearches", []):
        st.write(f"- {search.get('query', 'N/A')}")
