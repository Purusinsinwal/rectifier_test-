"""
Article Rectification System

This is where you implement your article rectification logic.
The run() function receives AI-generated content and should return the corrected version.

Feel free to:
- Add additional modules, classes, or helper functions
- Load and compare with source articles
- Implement multi-step validation and correction strategies
- Use multiple LLM calls or different models
- Add confidence scoring and logging
"""

from dotenv import load_dotenv
from litellm import completion
import os

load_dotenv()


def run(ai_generated_content: str, source_article_text: str) -> str:
    """
    Rectify an AI-generated article.
    
    Args:
        ai_generated_content: The AI-generated article text to be corrected
        source_article_text: The corresponding source article text for reference    
        
    Returns:
        str: The rectified article content

    """

    # Create a simple prompt to fix issues
    prompt = (
        "Fix all issues in the following article:\n\n"
        f"{ai_generated_content}\n\n"
        "Make sure to only change the parts that are incorrect or misleading and not the whole article. Keep the original style and tone."
        "Don't add any new word in the article just update the missing word and keep the original text intact."
        "You have to act as a surgeon not a writer. You have to fix the article and return only the corrected article text."
        "Use Source Article as reference to fix the article. If you find any missing word in the article then add it from the source article."
        f"{source_article_text}"
        "Return only the corrected article text." 
        "In Corrected format, return only the corrected article text without any extra information or explanation."
        
    )

    # Call LLM to rectify the article
    response = completion(
        model=os.getenv('LLM_MODEL_NAME'),
        messages=[
            {"role": "user", "content": prompt}
        ],
        api_key=os.getenv('LLM_API_KEY'),
        api_base=os.getenv('LLM_API_BASE')
    )
    
    rectified_content = response.choices[0].message.content.strip()
    return rectified_content    

