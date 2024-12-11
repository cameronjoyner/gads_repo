import os
import openai  # Use the OpenAI library

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Define the path to the HTML_DOCS folder and the output folder
html_docs_path = os.path.join(os.path.dirname(__file__), 'HTML_DOCS')
output_path = os.path.join(os.path.dirname(__file__), 'LLM_OUTPUT')

# Create the output directory if it doesn't exist
os.makedirs(output_path, exist_ok=True)

# Loop through each file in the HTML_DOCS directory
for filename in os.listdir(html_docs_path):
    if filename.endswith('.html'):  # Assuming the files are HTML
        print(f"Processing file: {filename}")  # Debugging statement
        file_path = os.path.join(html_docs_path, filename)
        
        # Read the content of the HTML file
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            print(f"Read content from {filename}, length: {len(html_content)}")  # Debugging statement
        
        # Define the prompt
        prompt = f"Please translate the following HTML into plain text without HTML markdown:\n{html_content}"
        
        print("Sending request to OpenAI API...")  # Debugging statement
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )

            # Get the response text
            output_text = response.choices[0].message.content
            
            # Save the output to a .txt file
            output_file_path = os.path.join(output_path, f'{os.path.splitext(filename)[0]}.txt')
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(output_text)
            
            # Print the return value
            print(f"Output saved to {output_file_path}")  # Debugging statement
            print(output_text)  # Debugging statement

        except Exception as e:
            print(f"An error occurred: {e}")  # Handle other exceptions
