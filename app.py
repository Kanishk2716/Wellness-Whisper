import os
import base64
import streamlit as st
from langchain.llms import Ollama
from langchain import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class MentalHealthAssistant:
    def __init__(self):
        # Topics Configuration
        self.topics = [
            "Anxiety", "Depression", "Stress", "Loneliness", "Coping Strategies", 
            "Support Systems", "Trauma and PTSD", "Emotional Regulation", 
            "Self-Esteem and Confidence", "Grief and Loss", "Work-Life Balance", 
            "Burnout Prevention", "Mindfulness and Meditation", "Anger Management", 
            "Relationships and Communication", "Sleep Disorders", "Eating Disorders", 
            "Substance Abuse", "ADHD and Focus Issues", "Bipolar Disorder", 
            "Social Anxiety", "Parenting Stress", "Chronic Illness and Mental Health"
        ]
        
        # Initialize LLM
        self.llm = Ollama(model="llama3.2", temperature=0.8)
        
        # Create Prompt Templates
        self.prompt_templates = self._create_prompt_templates()
        
        # Create Memories
        self.memories = self._create_memories()
        
        # Create Chains
        self.chains = self._create_chains()
        
        # Create Parent Chain
        self.parent_chain = self._create_parent_chain()

    def _create_prompt_templates(self):
        """Create prompt templates for different aspects of mental health"""
        template_configs = {
            'main_info': "Provide helpful and supportive information on mental health regarding {topic}.",
            'coping_strategies': "What are some coping strategies for dealing with {topic}?",
            'resources': "Please suggest some resources (like hotlines, websites, etc.) for someone seeking help with {topic}.",
            'self_care': "What are some self-care tips for managing {topic}?",
            'myths': "What are some common myths about {topic}?",
            'signs_symptoms': "What are the signs and symptoms of {topic}?",
            'when_to_seek_help': "When should someone seek help for {topic}?",
            'support_for_loved_ones': "How can I support a loved one dealing with {topic}?"
        }
        
        return {key: PromptTemplate(input_variables=['topic'], template=template) 
                for key, template in template_configs.items()}

    def _create_memories(self):
        """Create conversation memories for each chain"""
        return {key: ConversationBufferMemory(input_key='topic', memory_key=f'{key}_chat_history') 
                for key in self.prompt_templates.keys()}

    def _create_chains(self):
        """Create individual language model chains"""
        return {key: LLMChain(
            llm=self.llm, 
            prompt=self.prompt_templates[key], 
            verbose=True, 
            output_key=key, 
            memory=self.memories[key]
        ) for key in self.prompt_templates.keys()}

    def _create_parent_chain(self):
        """Create a sequential chain to process multiple aspects"""
        return SequentialChain(
            chains=list(self.chains.values()),
            input_variables=['topic'],
            output_variables=list(self.chains.keys()),
            verbose=True
        )

    def generate_response(self, topic):
        """Generate comprehensive mental health response"""
        return self.parent_chain({'topic': topic})

    def generate_markdown(self, response, topic):
        """Generate downloadable markdown content"""
        markdown_content = f"# Mental Health Information: {topic}\n\n"
        
        sections = [
            ('Information', 'main_info'),
            ('Coping Strategies', 'coping_strategies'),
            ('Self-Care Tips', 'self_care'),
            ('Common Myths', 'myths'),
            ('Signs and Symptoms', 'signs_symptoms'),
            ('When to Seek Help', 'when_to_seek_help'),
            ('Supporting Loved Ones', 'support_for_loved_ones'),
            ('Resources', 'resources')
        ]
        
        for title, key in sections:
            markdown_content += f"## {title}\n\n{response[key]}\n\n"
        
        return markdown_content

def main():
    # Streamlit UI Setup
    st.set_page_config(page_title="Mental Health Assistant", page_icon="🧠", layout="wide")
    st.title("Mental Health Assistance")
    
    # Sidebar Configuration
    st.sidebar.image("F:\\Kanishak\IPU\\IPU\\Projects\\Mental Health Assistant\\freepik__upload__85589.png", use_column_width=True)
    
    # Initialize Assistant
    assistant = MentalHealthAssistant()
    
    # Topic Selection
    selected_topic = st.selectbox(
        "Select a Mental Health Topic:", 
        ["Enter a custom topic..."] + assistant.topics
    )
    
    # Custom Topic Input
    input_text = st.text_input("Enter your own mental health topic:") if selected_topic == "Enter a custom topic..." else selected_topic
    
    # Generate Button
    if st.button("Generate Information"):
        if input_text:
            # Generate Response
            response = assistant.generate_response(input_text)
            
            # Display Response
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Information")
                st.write(response['main_info'])
                st.subheader("Coping Strategies")
                st.write(response['coping_strategies'])
                st.subheader("Self-Care Tips")
                st.write(response['self_care'])
                st.subheader("Common Myths")
                st.write(response['myths'])
            
            with col2:
                st.subheader("Signs and Symptoms")
                st.write(response['signs_symptoms'])
                st.subheader("When to Seek Help")
                st.write(response['when_to_seek_help'])
                st.subheader("Supporting Loved Ones")
                st.write(response['support_for_loved_ones'])
            
            st.subheader("Resources")
            st.write(response['resources'])
            
            # Download Button
            markdown_content = assistant.generate_markdown(response, input_text)
            b64 = base64.b64encode(markdown_content.encode()).decode()
            href = f'<a href="data:file/markdown;base64,{b64}" download="{input_text}_mental_health_info.md">Download Information</a>'
            st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Please select or enter a topic.")

    # Privacy Notice
    st.sidebar.markdown("""
    ⚠️ **Privacy Notice**
    - Information is confidential
    - No personal data stored
    - Seek professional help for serious concerns
    """)

if __name__ == "__main__":
    main()