import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from typing import Callable
from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(
        llm: Chain,
        portfolio: Portfolio,
        clean_text: Callable[[str], str]
) -> None:
    """
    Creates a Streamlit application for generating cold emails based on job descriptions.

    This function allows users to input a URL to a job posting, processes the content of
    the URL using a document loader and cleaning utility, extracts job details using the
    provided LLM (Large Language Model), and generates personalized emails for each job.

    Args:
        llm (Chain): An instance of the Chain class responsible for handling LLM operations,
                     such as extracting job details and generating emails.
        portfolio (Portfolio): An instance of the Portfolio class for querying relevant
                               portfolio links based on required job skills.
        clean_text (Callable[[str], str]): A function to clean and preprocess the text
                                           extracted from the job posting.

    Returns:
        None
    """
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-49485?from=job%20search%20funnel")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            # Load and clean job posting content
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Load portfolio and extract job details
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            # Generate emails for extracted jobs
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

