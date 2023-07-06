```python
import openai
from src.config import OPENAI_API_KEY
from src.utils import format_email_body

openai.api_key = OPENAI_API_KEY

def generate_email(donor):
    """
    Function to generate a customized email for a donor using GPT-3.5.
    """
    prompt = f"Dear {donor['name']},\n\nAs a valued supporter of our charity, we would like to update you on our recent activities and how your contributions have made a difference. Please personalize this message based on the donor's previous donations and alignment with the charity's mission."
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=200
    )

    email_body = format_email_body(response.choices[0].text.strip())
    return email_body
```