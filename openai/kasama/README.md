最初にターミナル上に環境変数を export します。

export OPENAI_API_KEY="sk-xxxx"

```python
import os
openai.api_key = os.environ["OPENAI_API_KEY"]
```

gpt-3.5-turbo を model として使用するには upgrade が必要そう

```
pip install --upgrade pip
```

実行文

```cmd
streamlit run app_chatgpt_test.py
```
