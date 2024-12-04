# Wellness Whisper 🌈
Mental Health Assistant

WellnessWhisper is an intuitive and accessible application designed to empower users with valuable information and resources on mental health and well-being. Leveraging cutting-edge technologies like LangChain, Ollama, and Streamlit, WellnessWhisper provides personalized guidance to help users understand, navigate, and manage mental health challenges. Whether you're seeking educational insights, coping strategies, or supportive resources, WellnessWhisper is your reliable companion for holistic mental wellness.

---
## Features 🚀 
-Topic Selection: Choose from predefined mental health topics or input custom topics using natural language.

-Comprehensive Responses: Receive detailed insights, coping strategies, self-care tips, and more tailored to the selected topic.

-Downloadable Content: Export generated information as markdown files for offline access.

-Privacy Notice: We prioritize your privacy—no personal data is stored. For serious concerns, users are encouraged to seek professional help.

### 📥 Download Options  
- Export generated analyses as a markdown file for your convenience.

  ---

## Tech Stack 💻  

- **Frontend:** [Streamlit](https://streamlit.io/) for an interactive and user-friendly UI.
- **Backend:**  
  - `LangChain 🤖`: Managing language model chains and memory.
  - `Ollama`: Providing a powerful large language model (LLM).
  - `dotenv`: Managing environment variables securely.
- **Deployment:** Python-based for simplicity and lightweight requirements.

  ---

## Installation 🔧

1. Clone the repository:  
   
    ```bash
    git clone https://github.com/kanishk-tehwatia/WellnessWhisper.git
    cd WellnessWhisper
    ```

2. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

# Usage Guide 📖

1. Select a Topic:

   Choose from a list of predefined mental health topics.
   Alternatively, input a custom topic using natural language for a personalized experience.

2. Generate Insights:

   Click on the "Generate Insights" button to receive detailed information, coping strategies, self-care tips, and other valuable     
   resources.

3. Download Content:

   Save the generated information as a markdown file for offline reference.

4. Explore More:

   Use the sidebar to revisit and explore previously generated insights.

```bash
  WellnessWhisper/
  ├── app.py               # Main application code
  ├── requirements.txt     # Python dependencies
  ├── .env.example         # Example environment variable file
  ├── README.md            # Project documentation
  ├── topics/              # Folder for predefined mental health topics (optional)
  └── downloads/           # Folder for storing downloaded analyses
```

# Fork the repository.

 - Create your feature branch: git checkout -b feature-name.
 - Commit your changes: git commit -m 'Add feature'.
 - Push to the branch: git push origin feature-name.
 - Open a Pull Request.
