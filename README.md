# Step Setup for Python Workshop 02
  
- Run the following commands in your terminal:
```bash
uv sync
```
- open `example.py` in your code editor and edit the API keys as needed. 
  or run the following command to set your API keys in the terminal:
```bash
export OPENAI_API_KEY="your_openai_api_key"
export GOOGLE_API_KEY="your_google_api_key"
export ANTHROPIC_API_KEY="your_anthropic_api_key"
```

- Run the code:
```bash
uv run example.py
```
if output is not as expected, check the API keys and ensure they are correct.

# Steps to Complete the Workshop

1.  **Write Your Tools**: Open `main.py` and write at least 3 of your own custom tools.

2.  **Use Your Tools**: In the same file (`main.py`), find the "Run the Agent and Observe" section and modify it to use the tools you just created.

3.  **Test Your Code**: Run the script to make sure everything works as expected.
    ```bash
    uv run main.py
    ```

4.  **Capture Your Code And Output**: After running the script, take a screenshot of your code and the output in your terminal. Ensure that the output shows the results of the prompts you used with your custom tools.

       - On macOS, you can use `Command + Shift + 4` to take a screenshot of a selected area.
       - On Windows, you can use `Windows + Shift + S` to capture a specific area of your screen.
       - On Linux, you can use `gnome-screenshot` or similar tools depending on your desktop environment.

5.  **Submit Your Work**: Upload the screenshot to the designated platform or share it with your instructor as per the workshop guidelines.

6.  **Congratulate yourself!** You've completed the workshop.
