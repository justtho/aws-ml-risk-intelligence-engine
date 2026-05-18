# Current Solution Architecture

## Workflow

User Input
→ Streamlit UI
→ ML Classification Model
→ Semantic Search (FAISS Vector Store)
→ Similar Case Retrieval
→ LLM Risk Summary Generation
→ Prediction Logging
→ Monitoring & Validation

## Components

### Streamlit
Frontend application for user interaction.

### ML Classification Engine
TF-IDF + Logistic Regression model for financial risk categorization.

### Semantic Search Layer
FAISS vector database used for similarity search and contextual retrieval.

### LLM Layer
OpenAI GPT model used for AI-generated risk summaries.

### Monitoring
Prediction logging and validation metrics for observability.