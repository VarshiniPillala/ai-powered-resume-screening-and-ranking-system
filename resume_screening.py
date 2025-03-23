import streamlit as st
import pdfplumber
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from io import BytesIO

def extract_pdf_text(file):
    """Extract text content from a PDF file."""
    extracted_text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            extracted_text += page.extract_text() + "\n"
    return extracted_text.strip()

def compute_similarity_scores(job_desc, resumes, skill_weight=1.0, experience_weight=1.0):
    """Compute similarity scores for resumes based on the job description."""
    all_documents = [job_desc] + resumes
    tfidf_vectorizer = TfidfVectorizer().fit_transform(all_documents)
    vectors = tfidf_vectorizer.toarray()

    job_vector = vectors[0]
    resume_vectors = vectors[1:]
    similarity_scores = cosine_similarity([job_vector], resume_vectors).flatten()

    # Adjust scores based on specified weights
    adjusted_scores = similarity_scores * skill_weight * experience_weight
    return adjusted_scores

def emphasize_keywords(text, keywords):
    """Highlight job description keywords in resumes."""
    for keyword in keywords:
        text = re.sub(f'(?i)\\b{re.escape(keyword)}\\b', f'**{keyword}**', text)
    return text

def create_csv_download_link(data_frame):
    """Generate a download link for the ranked results as a CSV file."""
    buffer = BytesIO()
    data_frame.to_csv(buffer, index=False)
    buffer.seek(0)
    return buffer

# Streamlit UI components
st.title("AI-Powered Resume Screening & Ranking Tool")

# Job description input
st.header("Enter Job Description")
job_desc_input = st.text_area("Job Description", placeholder="Paste job description here...")

# Sidebar for adjusting weights
st.sidebar.header("Adjust Ranking Weights")
skills_weight = st.sidebar.slider("Skill Weight", 0.5, 2.0, 1.0)
experience_weight = st.sidebar.slider("Experience Weight", 0.5, 2.0, 1.0)

# File uploader for resumes
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Select PDF resumes", type=["pdf"], accept_multiple_files=True)

if uploaded_files and job_desc_input:
    st.header("Ranked Resumes")

    # Extract text from the uploaded resumes
    resume_texts = [extract_pdf_text(file) for file in uploaded_files]

    # Extract keywords from the job description
    job_keywords = job_desc_input.split()

    # Compute the similarity scores for each resume
    similarity_scores = compute_similarity_scores(job_desc_input, resume_texts, skills_weight, experience_weight)

    # Prepare the results
    ranking_data = pd.DataFrame({"Resume": [file.name for file in uploaded_files], "Score": similarity_scores})
    ranking_data = ranking_data.sort_values(by="Score", ascending=False)

    # Display ranked resumes
    st.write(ranking_data)

    # Visualization - Bar Chart
    st.subheader("Resume Ranking Visualization")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(ranking_data["Resume"], ranking_data["Score"], color='lightblue')
    ax.set_xlabel("Ranking Score")
    ax.set_ylabel("Resume")
    ax.set_title("Resume Ranking Based on Job Description Similarity")
    st.pyplot(fig)

    # Highlight keywords in top-ranked resumes
    st.subheader("Highlighted Keywords in Top Resumes")
    for _, row in ranking_data.iterrows():
        resume_text = extract_pdf_text(uploaded_files[ranking_data.index.get_loc(row.name)])
        highlighted_resume = emphasize_keywords(resume_text, job_keywords)
        with st.expander(f"{row['Resume']} - Score: {row['Score']:.2f}"):
            st.markdown(highlighted_resume)

    # CSV Export Button
    st.download_button("Download Rankings as CSV", create_csv_download_link(ranking_data), "ranked_resumes.csv", "text/csv")
