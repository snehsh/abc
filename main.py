import streamlit as st
from graphs.pie_chart.pie_chart_apac_totalticketcount import pie_chart_apac_totalticketcount, \
    pie_chart_emea_totalticketcount, pie_chart_nam_totalticketcount, pie_chart_cala_totalticketcount
from graphs.bar_graph.bar_graph_apac_prod_nonprod import bar_graph_apac_prod_nonprod, bar_graph_emea_prod_nonprod, \
    bar_graph_cala_prod_nonprod, bar_graph_nam_prod_nonprod
from openai import OpenAI
from streamlit.components.v1 import html

st.title("Welcome")




COLOR_MAPPING = {
    'CompanyA': 'brown',
    'CompanyB': 'skyblue',
    'CompanyC': 'green',
    'CompanyD': 'orange'
}


def main():
    # Create tabs
    tab1, tab2 = st.tabs(["Analysis", "Chat Bot"])

    with tab1:

        regions = ["APAC", "EMEA", "CALA", "NAM"]
        selected_region = st.selectbox("Regions", regions, index=None)

        if selected_region == "APAC":
            analysis_type = ["Total Count of Tickets", "Stream Based Distribution", "Prod/Non-Prod Distribution",
                             "Resolution Category L2 Analysis", "Resolution Category L3 Analysis", "MTTR Analysis",
                             "Resolution Based Analysis", "Inc Summary Analysis", "Product Based Distribution"]
            selected_analysis_type = st.selectbox("Analysis Type", analysis_type, index=None)

            if selected_analysis_type == "Total Count of Tickets":
                pie_chart_apac_totalticketcount()

            elif selected_analysis_type == "Stream Based Distribution":
                st.write("Graph2")

            elif selected_analysis_type == "Prod/Non-Prod Distribution":
                bar_graph_apac_prod_nonprod()

            elif selected_analysis_type == "Resolution Category L2 Analysis":
                st.write("Graph4")
            elif selected_analysis_type == "Resolution Category L3 Analysis":
                st.write("Graph5")
            elif selected_analysis_type == "MTTR Analysis":
                st.write("Graph6")
            elif selected_analysis_type == "Resolution Based Analysis":
                st.write("Graph7")
            elif selected_analysis_type == "Inc Summary Analysis":
                st.write("Graph8")
            elif selected_analysis_type == "Product Based Distribution":
                st.write("Graph9")

        if selected_region == "EMEA":
            analysis_type = ["Total Count of Tickets", "Stream Based Distribution", "Prod/Non-Prod Distribution",
                             "Resolution Category L2 Analysis", "Resolution Category L3 Analysis", "MTTR Analysis",
                             "Resolution Based Analysis", "Inc Summary Analysis", "Product Based Distribution"]
            selected_analysis_type = st.selectbox("Analysis Type", analysis_type, index=None)

            if selected_analysis_type == "Total Count of Tickets":
                pie_chart_emea_totalticketcount()

            elif selected_analysis_type == "Stream Based Distribution":
                st.write("Graph2")

            elif selected_analysis_type == "Prod/Non-Prod Distribution":
                bar_graph_emea_prod_nonprod()

            elif selected_analysis_type == "Resolution Category L2 Analysis":
                st.write("Graph4")
            elif selected_analysis_type == "Resolution Category L3 Analysis":
                st.write("Graph5")
            elif selected_analysis_type == "MTTR Analysis":
                st.write("Graph6")
            elif selected_analysis_type == "Resolution Based Analysis":
                st.write("Graph7")
            elif selected_analysis_type == "Inc Summary Analysis":
                st.write("Graph8")
            elif selected_analysis_type == "Product Based Distribution":
                st.write("Graph9")

        if selected_region == "CALA":
            analysis_type = ["Total Count of Tickets", "Stream Based Distribution", "Prod/Non-Prod Distribution",
                             "Resolution Category L2 Analysis", "Resolution Category L3 Analysis", "MTTR Analysis",
                             "Resolution Based Analysis", "Inc Summary Analysis", "Product Based Distribution"]
            selected_analysis_type = st.selectbox("Analysis Type", analysis_type, index=None)

            if selected_analysis_type == "Total Count of Tickets":
                pie_chart_cala_totalticketcount()

            elif selected_analysis_type == "Stream Based Distribution":
                st.write("Graph2")

            elif selected_analysis_type == "Prod/Non-Prod Distribution":
                bar_graph_cala_prod_nonprod()

            elif selected_analysis_type == "Resolution Category L2 Analysis":
                st.write("Graph4")
            elif selected_analysis_type == "Resolution Category L3 Analysis":
                st.write("Graph5")
            elif selected_analysis_type == "MTTR Analysis":
                st.write("Graph6")
            elif selected_analysis_type == "Resolution Based Analysis":
                st.write("Graph7")
            elif selected_analysis_type == "Inc Summary Analysis":
                st.write("Graph8")
            elif selected_analysis_type == "Product Based Distribution":
                st.write("Graph9")

        if selected_region == "NAM":
            analysis_type = ["Total Count of Tickets", "Stream Based Distribution", "Prod/Non-Prod Distribution",
                             "Resolution Category L2 Analysis", "Resolution Category L3 Analysis", "MTTR Analysis",
                             "Resolution Based Analysis", "Inc Summary Analysis", "Product Based Distribution"]
            selected_analysis_type = st.selectbox("Analysis Type", analysis_type, index=None)

            if selected_analysis_type == "Total Count of Tickets":
                pie_chart_nam_totalticketcount()

            elif selected_analysis_type == "Stream Based Distribution":
                st.write("Graph2")

            elif selected_analysis_type == "Prod/Non-Prod Distribution":
                bar_graph_nam_prod_nonprod()

            elif selected_analysis_type == "Resolution Category L2 Analysis":
                st.write("Graph4")
            elif selected_analysis_type == "Resolution Category L3 Analysis":
                st.write("Graph5")
            elif selected_analysis_type == "MTTR Analysis":
                st.write("Graph6")
            elif selected_analysis_type == "Resolution Based Analysis":
                st.write("Graph7")
            elif selected_analysis_type == "Inc Summary Analysis":
                st.write("Graph8")
            elif selected_analysis_type == "Product Based Distribution":
                st.write("Graph9")

    # Set session state for the active tab when About tab is selected
    with tab2:
        from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

        st.title("ChatBot")

        # Load the Hugging Face model and tokenizer
        model_name = "openai-community/gpt2"


        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = chatbot(prompt, max_length=100, num_return_sequences=1)
                response_text = response[0]["generated_text"]
                st.markdown(response_text)
            st.session_state.messages.append({"role": "assistant", "content": response_text})

if __name__ == "__main__":
    main()
