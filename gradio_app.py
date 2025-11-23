import gradio as gr
import random

def analyze_news(news_text):
    """
    Analyze news text for fake news detection.
    Replace this with your actual ML model prediction logic.
    """
    if not news_text or len(news_text.strip()) < 10:
        return "Please enter a valid news article (at least 10 characters).", None, None
    
    # TODO: Replace with your actual model prediction
    # Example: prediction = your_model.predict(news_text)
    
    # Mock analysis for demonstration
    fake_keywords = ['shocking', 'unbelievable', 'secret', 'they don\'t want you to know']
    has_fake_keywords = any(keyword in news_text.lower() for keyword in fake_keywords)
    
    # Simulate prediction
    is_fake = has_fake_keywords or random.random() > 0.6
    confidence = random.randint(65, 95)
    
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
