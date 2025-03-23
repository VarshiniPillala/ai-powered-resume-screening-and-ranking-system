AI-powered-resume-screening-and-ranking-system
The "AI-Powered Resume Screening and Ranking System" is an automated solution that helps recruiters and HR professionals quickly rank resumes based on their relevance to a job description. The system processes PDF resumes and provides ranked results with similarity scores.
Certainly! Here's the updated version without emojis, maintaining a more professional tone:

---

AI-Powered Resume Screening and Ranking System

This innovative AI-powered system streamlines the process of resume screening and ranking, using a combination of Streamlit, scikit-learn, and PyPDF2. The application allows users to upload resumes in PDF format, compares them with a provided job description, and ranks them based on cosine similarity using TF-IDF.

Key Features:
- Upload multiple PDF resumes at once.
- Input a job description for comparison.
- Ranks resumes using TF-IDF and Cosine Similarity.
- Displays resumes with ranked similarity scores.

Project Structure:
resume_screening_app/
│── .venv/
│── app.py
│── requirements.txt
├── resume_ranking.ipynb
│── data/
│   ├── sample_resume.pdf
│── README.md
│── .gitignore


Installation & Setup:
1. Clone the repository to your local machine.
2. (Optional) Create a virtual environment:
```bash
python -m venv .venv
```
- Activate the environment:
  - Windows: `source .venv\Scripts\activate`
  - Mac/Linux: `source .venv/bin/activate`
3. Install the required dependencies:
```bash
pip install -r requirements.txt
```
4. Launch the app with Streamlit:
```bash
streamlit run app.py
```
Your browser will automatically open the app.

How It Works:
1. Upload resumes in PDF format through the file uploader.
2. Enter the job description into the provided text box.
3. The system processes the resumes, converting them into TF-IDF vectors.
4. The job description is compared to each resume using cosine similarity.
5. Ranked resumes, along with similarity scores, are displayed.

Deployment:
To deploy on Streamlit Cloud (Free):
1. Push your project to GitHub.
2. Log into Streamlit Cloud
3. Click New App select your GitHub repository, and point to `app.py`.
4. Click Deploy

Requirements:
- streamlit
- PyPDF2
- pandas
- scikit-learn
- numpy

Install all dependencies by running:
```bash
pip install -r requirements.txt
```

Target Users:
- HR Professionals & Recruiters – Automate the resume screening process for quicker hires.
- Hiring Managers – Rank resumes quickly for open roles.
- Job Portals – Improve accuracy in matching resumes to job descriptions.
- AI Enthusiasts & Students – Gain hands-on experience with NLP-based resume analysis.

Future Enhancements:
- AI-Based Scoring – Implement ML or deep learning for better ranking.
- Advanced NLP – Incorporate models like BERT or GPT for deeper analysis.
- Multi-Format Support – Extend support to DOCX, TXT files, and OCR for image-based resumes.
- Automatic Skill Matching – Extract skills and experience for enhanced ranking.
- API Integration – Seamlessly connect with job portals and HR systems.

Conclusion:
This "AI-powered Resume Screening & Ranking System" significantly reduces the time and effort of manual resume screening, providing an efficient and scalable solution for recruiters, hiring managers, and job portals. By utilizing TF-IDF and Cosine Similarity, the system ensures quick, accurate, and unbiased candidate shortlisting. With easy deployment via Streamlit and real-time ranking, this project offers an intuitive tool for anyone involved in recruitment.

[Streamlit Cloud Deployment](https://ai-powered-resume-screening-and-ranking-system-6925.streamlit.app)
