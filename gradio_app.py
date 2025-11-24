import gradio as gr
import pickle
import numpy as np
import re
import string

# Load your trained model (place your model.pkl file in the same directory)
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully!")
except FileNotFoundError:
    print("Warning: model.pkl not found. Using mock predictions.")
    model = None

def preprocess_text(text):
    """
    Preprocess text before feeding to the model.
    Adjust this based on how you preprocessed your training data.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

def analyze_news(news_text):
    """
    Analyze news text for fake news detection using trained ML model.
    """
    if not news_text or len(news_text.strip()) < 10:
        return "Please enter a valid news article (at least 10 characters).", None, None
    
    # Preprocess the text
    processed_text = preprocess_text(news_text)
    
    if model is not None:
        try:
            # Get prediction probabilities
            # Note: Adjust this based on your model's expected input format
            # If your model uses TfidfVectorizer or CountVectorizer, you'll need to load that too
            probabilities = model.predict_proba([processed_text])[0]
            
            # Assuming binary classification: [Real, Fake] or [Fake, Real]
            # Adjust index based on your model's label ordering
            fake_probability = probabilities[1] if len(probabilities) > 1 else probabilities[0]
            confidence = int(fake_probability * 100)
            is_fake = fake_probability > 0.5
        except Exception as e:
            print(f"Prediction error: {e}")
            # Fallback to mock prediction
            is_fake = len(processed_text) % 2 == 0
            confidence = 75
    else:
        # Mock prediction when model is not loaded
        is_fake = len(processed_text) % 2 == 0
        confidence = 75
    
    if is_fake:
        label = "⚠️ Fake News Detected"
        color = "#ef4444"
        analysis = f"This article shows signs of misinformation. Confidence: {confidence}%. Consider verifying with reliable sources."
    else:
        label = "✓ Appears to be Real News"
        color = "#10b981"
        analysis = f"This article appears legitimate. Confidence: {confidence}%. Always cross-reference important information."
    
    # Return styled HTML result
    result_html = f"""
    <div style="padding: 20px; border-radius: 8px; border: 2px solid {color}; background: {color}15;">
        <h2 style="color: {color}; margin: 0 0 10px 0;">{label}</h2>
        <p style="margin: 10px 0;"><strong>Confidence Score:</strong> {confidence}%</p>
        <div style="background: #f3f4f6; border-radius: 4px; height: 8px; overflow: hidden; margin: 10px 0;">
            <div style="background: {color}; height: 100%; width: {confidence}%;"></div>
        </div>
        <p style="margin: 10px 0; color: #6b7280;">{analysis}</p>
    </div>
    """
    
    return result_html, confidence, "Fake" if is_fake else "Real"


# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft(), title="Fake News Detector") as demo:
    gr.Markdown(
        """
        # 🔍 Fake News Detection System
        
        Enter a news article below to analyze its authenticity using AI-powered detection.
        
        **Note:** This is a demonstration. Replace the mock analysis with your trained ML model for production use.
        """
    )
    
    with gr.Row():
        with gr.Column(scale=2):
            news_input = gr.Textbox(
                label="Enter News Article",
                placeholder="Paste the news article text here...",
                lines=10,
                max_lines=20
            )
            
            with gr.Row():
                clear_btn = gr.Button("Clear", variant="secondary")
                analyze_btn = gr.Button("Analyze News", variant="primary")
            
            char_count = gr.Textbox(
                label="Character Count",
                interactive=False,
                scale=1
            )
        
        with gr.Column(scale=2):
            result_output = gr.HTML(label="Analysis Result")
            
            with gr.Row():
                confidence_output = gr.Number(label="Confidence %", interactive=False)
                classification_output = gr.Textbox(label="Classification", interactive=False)
    
    # Example articles
    gr.Markdown("### 📰 Try These Examples:")
    gr.Examples(
        examples=[
            ["Scientists at MIT have discovered a new renewable energy source that could replace fossil fuels. The research, published in Nature, shows promising results from initial tests."],
            ["SHOCKING: Secret government files reveal unbelievable truth they don't want you to know! Click here to learn more about this conspiracy."],
            ["The stock market closed higher today as investors responded positively to the latest economic data. The S&P 500 gained 1.2% while the Dow Jones increased by 0.8%."]
        ],
        inputs=news_input,
        label="Sample Articles"
    )
    
    # Update character count
    news_input.change(
        fn=lambda x: f"{len(x)} characters",
        inputs=news_input,
        outputs=char_count
    )
    
    # Analyze button click
    analyze_btn.click(
        fn=analyze_news,
        inputs=news_input,
        outputs=[result_output, confidence_output, classification_output]
    )
    
    # Clear button click
    clear_btn.click(
        fn=lambda: ("", "", None, None),
        outputs=[news_input, result_output, confidence_output, classification_output]
    )
    
    gr.Markdown(
        """
        ---
        **Disclaimer:** This tool is for demonstration purposes. Always verify news from multiple reliable sources.
        """
    )

# Launch the app
if __name__ == "__main__":
    demo.launch(
        share=False,  # Set to True to create a public link
        server_name="0.0.0.0",  # Makes it accessible on your network
        server_port=7860
    )
