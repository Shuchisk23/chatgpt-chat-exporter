# # # # # # # import streamlit as st
# # # # # # # from selenium import webdriver
# # # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # # from selenium.webdriver.common.by import By
# # # # # # # from fpdf import FPDF
# # # # # # # import time

# # # # # # # st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# # # # # # # st.title("📄 Export ChatGPT Shared Chat to PDF")

# # # # # # # url = st.text_input("Paste your ChatGPT shared link:")

# # # # # # # chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # update this!

# # # # # # # def remove_emojis(text):
# # # # # # #     return text.encode('ascii', 'ignore').decode('ascii')

# # # # # # # def fetch_chat_with_selenium(url):
# # # # # # #     chrome_options = Options()
# # # # # # #     chrome_options.add_argument("--headless=new")
# # # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # # #     chrome_options.add_argument("--no-sandbox")

# # # # # # #     service = Service(chromedriver_path)
# # # # # # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # # # # # #     driver.get(url)
# # # # # # #     time.sleep(5)  # wait for full page load

# # # # # # #     chat = []

# # # # # # #     # Grab all message containers
# # # # # # #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# # # # # # #     for container in containers:
# # # # # # #         role = container.get_attribute("data-message-author-role")

# # # # # # #         try:
# # # # # # #             # Try to get markdown (assistant usually uses this)
# # # # # # #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# # # # # # #             message_text = message_elem.text.strip()
# # # # # # #         except:
# # # # # # #             # If no markdown, get raw innerText (usually user)
# # # # # # #             message_text = container.text.strip()

# # # # # # #         if message_text:
# # # # # # #             if role == "user":
# # # # # # #                 chat.append(("User", message_text))
# # # # # # #             elif role == "assistant":
# # # # # # #                 chat.append(("ChatGPT", message_text))

# # # # # # #     driver.quit()
# # # # # # #     return chat

# # # # # # # if st.button("Fetch & Export"):
# # # # # # #     if url:
# # # # # # #         try:
# # # # # # #             with st.spinner("Fetching and formatting chat..."):
# # # # # # #                 chat = fetch_chat_with_selenium(url)

# # # # # # #                 # Show in Streamlit
# # # # # # #                 for speaker, message in chat:
# # # # # # #                     emoji = "🧑" if speaker == "User" else "🤖"
# # # # # # #                     st.markdown(f"**{emoji} {speaker}**:\n{message}\n---")

# # # # # # #                 # Export to PDF
# # # # # # #                 pdf = FPDF()
# # # # # # #                 pdf.add_page()
# # # # # # #                 pdf.set_font("Arial", size=12)
# # # # # # #                 for speaker, message in chat:
# # # # # # #                     prefix = f"{speaker}: "
# # # # # # #                     clean_text = remove_emojis(message)
# # # # # # #                     pdf.multi_cell(0, 10, prefix + clean_text + "\n")

# # # # # # #                 pdf_path = "chatgpt_chat.pdf"
# # # # # # #                 pdf.output(pdf_path)

# # # # # # #                 with open(pdf_path, "rb") as f:
# # # # # # #                     st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

# # # # # # #         except Exception as e:
# # # # # # #             st.error(f"❌ Error: {e}")

# # # # # # import streamlit as st
# # # # # # from selenium import webdriver
# # # # # # from selenium.webdriver.chrome.service import Service
# # # # # # from selenium.webdriver.chrome.options import Options
# # # # # # from selenium.webdriver.common.by import By
# # # # # # from fpdf import FPDF
# # # # # # import time

# # # # # # st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# # # # # # st.title("📄 Export ChatGPT Shared Chat to PDF")

# # # # # # url = st.text_input("Paste your ChatGPT shared link:")

# # # # # # chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # update this!

# # # # # # def remove_emojis(text):
# # # # # #     return text.encode('ascii', 'ignore').decode('ascii')

# # # # # # def fetch_chat_with_selenium(url):
# # # # # #     chrome_options = Options()
# # # # # #     chrome_options.add_argument("--headless=new")
# # # # # #     chrome_options.add_argument("--disable-gpu")
# # # # # #     chrome_options.add_argument("--no-sandbox")

# # # # # #     service = Service(chromedriver_path)
# # # # # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # # # # #     driver.get(url)
# # # # # #     time.sleep(5)

# # # # # #     chat = []
# # # # # #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# # # # # #     for container in containers:
# # # # # #         role = container.get_attribute("data-message-author-role")
# # # # # #         try:
# # # # # #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# # # # # #             message_text = message_elem.text.strip()
# # # # # #         except:
# # # # # #             message_text = container.text.strip()

# # # # # #         if message_text:
# # # # # #             if role == "user":
# # # # # #                 chat.append(("User", message_text))
# # # # # #             elif role == "assistant":
# # # # # #                 chat.append(("ChatGPT", message_text))

# # # # # #     driver.quit()
# # # # # #     return chat

# # # # # # # Fancy PDF generator
# # # # # # class ChatPDF(FPDF):
# # # # # #     def header(self):
# # # # # #         self.set_font("Arial", 'B', 14)
# # # # # #         self.cell(0, 10, "ChatGPT Conversation", ln=True, align="C")
# # # # # #         self.ln(5)

# # # # # #     def add_message(self, speaker, message):
# # # # # #         self.set_font("Arial", "B", 12)
# # # # # #         self.set_text_color(0)
# # # # # #         self.multi_cell(0, 8, f"{speaker}:", ln=1)
# # # # # #         self.ln(1)

# # # # # #         self.set_font("Arial", "", 12)
# # # # # #         lines = message.split('\n')
# # # # # #         in_code_block = False

# # # # # #         for line in lines:
# # # # # #             stripped = line.strip()

# # # # # #             # Code block start/end
# # # # # #             if stripped.startswith("```"):
# # # # # #                 in_code_block = not in_code_block
# # # # # #                 if in_code_block:
# # # # # #                     self.set_fill_color(230, 230, 230)
# # # # # #                     self.multi_cell(0, 6, "", ln=1, fill=True)  # top spacing
# # # # # #                 continue

# # # # # #             if in_code_block:
# # # # # #                 self.set_font("Courier", "", 11)
# # # # # #                 self.set_fill_color(240, 240, 240)
# # # # # #                 self.multi_cell(0, 6, line, ln=1, fill=True)
# # # # # #                 self.set_font("Arial", "", 12)
# # # # # #             elif stripped.startswith("- ") or stripped.startswith("•"):
# # # # # #                 self.cell(5)
# # # # # #                 self.multi_cell(0, 6, u"\u2022 " + stripped[2:])
# # # # # #             elif any(stripped.startswith(f"{n}. ") for n in range(1, 10)):
# # # # # #                 self.multi_cell(0, 6, stripped)
# # # # # #             else:
# # # # # #                 self.multi_cell(0, 6, line)

# # # # # #         self.ln(4)

# # # # # # if st.button("Fetch & Export"):
# # # # # #     if url:
# # # # # #         try:
# # # # # #             with st.spinner("Fetching and formatting chat..."):
# # # # # #                 chat = fetch_chat_with_selenium(url)

# # # # # #                 for speaker, message in chat:
# # # # # #                     emoji = "🧑" if speaker == "User" else "🤖"
# # # # # #                     st.markdown(f"**{emoji} {speaker}**:\n{message}\n---")

# # # # # #                 pdf = ChatPDF()
# # # # # #                 pdf.add_page()
# # # # # #                 pdf.set_auto_page_break(auto=True, margin=15)

# # # # # #                 for speaker, message in chat:
# # # # # #                     clean_text = remove_emojis(message)
# # # # # #                     pdf.add_message(speaker, clean_text)

# # # # # #                 pdf_path = "chatgpt_chat.pdf"
# # # # # #                 pdf.output(pdf_path)

# # # # # #                 with open(pdf_path, "rb") as f:
# # # # # #                     st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

# # # # # #         except Exception as e:
# # # # # #             st.error(f"❌ Error: {e}")

# # # # # import streamlit as st
# # # # # from selenium import webdriver
# # # # # from selenium.webdriver.chrome.service import Service
# # # # # from selenium.webdriver.chrome.options import Options
# # # # # from selenium.webdriver.common.by import By
# # # # # from fpdf import FPDF
# # # # # import time

# # # # # st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# # # # # st.title("📄 Export ChatGPT Shared Chat to PDF")

# # # # # url = st.text_input("Paste your ChatGPT shared link:")

# # # # # chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # update this!

# # # # # def remove_emojis(text):
# # # # #     return text.encode('ascii', 'ignore').decode('ascii')

# # # # # def fetch_chat_with_selenium(url):
# # # # #     chrome_options = Options()
# # # # #     chrome_options.add_argument("--headless=new")
# # # # #     chrome_options.add_argument("--disable-gpu")
# # # # #     chrome_options.add_argument("--no-sandbox")

# # # # #     service = Service(chromedriver_path)
# # # # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # # # #     driver.get(url)
# # # # #     time.sleep(5)

# # # # #     chat = []
# # # # #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# # # # #     for container in containers:
# # # # #         role = container.get_attribute("data-message-author-role")
# # # # #         try:
# # # # #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# # # # #             message_text = message_elem.text.strip()
# # # # #         except:
# # # # #             message_text = container.text.strip()

# # # # #         if message_text:
# # # # #             if role == "user":
# # # # #                 chat.append(("User", message_text))
# # # # #             elif role == "assistant":
# # # # #                 chat.append(("ChatGPT", message_text))

# # # # #     driver.quit()
# # # # #     return chat

# # # # # # Fancy PDF generator
# # # # # class ChatPDF(FPDF):
# # # # #     def header(self):
# # # # #         self.set_font("Arial", 'B', 14)
# # # # #         self.cell(0, 10, "ChatGPT Conversation", align="C")
# # # # #         self.ln(10)

# # # # #     def add_message(self, speaker, message):
# # # # #         self.set_font("Arial", "B", 12)
# # # # #         self.set_text_color(0)
# # # # #         self.multi_cell(0, 8, f"{speaker}:")
# # # # #         self.ln(1)

# # # # #         self.set_font("Arial", "", 12)
# # # # #         lines = message.split('\n')
# # # # #         in_code_block = False

# # # # #         for line in lines:
# # # # #             stripped = line.strip()

# # # # #             # Detect start/end of code block
# # # # #             if stripped.startswith("```"):
# # # # #                 in_code_block = not in_code_block
# # # # #                 if in_code_block:
# # # # #                     self.set_fill_color(230, 230, 230)
# # # # #                     self.ln(1)
# # # # #                 continue

# # # # #             if in_code_block:
# # # # #                 self.set_font("Courier", "", 11)
# # # # #                 self.set_fill_color(240, 240, 240)
# # # # #                 self.multi_cell(0, 6, line, fill=True)
# # # # #                 self.set_font("Arial", "", 12)
# # # # #             elif stripped.startswith("- ") or stripped.startswith("•"):
# # # # #                 self.cell(5)
# # # # #                 self.multi_cell(0, 6, u"\u2022 " + stripped[2:])
# # # # #             elif any(stripped.startswith(f"{n}. ") for n in range(1, 10)):
# # # # #                 self.multi_cell(0, 6, stripped)
# # # # #             else:
# # # # #                 self.multi_cell(0, 6, line)

# # # # #         self.ln(4)

# # # # # if st.button("Fetch & Export"):
# # # # #     if url:
# # # # #         try:
# # # # #             with st.spinner("Fetching and formatting chat..."):
# # # # #                 chat = fetch_chat_with_selenium(url)

# # # # #                 for speaker, message in chat:
# # # # #                     emoji = "🧑" if speaker == "User" else "🤖"
# # # # #                     st.markdown(f"**{emoji} {speaker}**:\n{message}\n---")

# # # # #                 pdf = ChatPDF()
# # # # #                 pdf.add_page()
# # # # #                 pdf.set_auto_page_break(auto=True, margin=15)

# # # # #                 for speaker, message in chat:
# # # # #                     clean_text = remove_emojis(message)
# # # # #                     pdf.add_message(speaker, clean_text)

# # # # #                 pdf_path = "chatgpt_chat.pdf"
# # # # #                 pdf.output(pdf_path)

# # # # #                 with open(pdf_path, "rb") as f:
# # # # #                     st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

# # # # #         except Exception as e:
# # # # #             st.error(f"❌ Error: {e}")

# # # # import streamlit as st
# # # # from selenium import webdriver
# # # # from selenium.webdriver.chrome.service import Service
# # # # from selenium.webdriver.chrome.options import Options
# # # # from selenium.webdriver.common.by import By
# # # # from fpdf import FPDF
# # # # import time

# # # # # Streamlit UI
# # # # st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# # # # st.title("📄 Export ChatGPT Shared Chat to PDF")

# # # # url = st.text_input("Paste your ChatGPT shared link:")

# # # # chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # 🔁 Change this to your path

# # # # # Clean emojis for PDF compatibility
# # # # def remove_emojis(text):
# # # #     return text.encode('ascii', 'ignore').decode('ascii')

# # # # # Fetch chat from ChatGPT shared link
# # # # def fetch_chat_with_selenium(url):
# # # #     chrome_options = Options()
# # # #     chrome_options.add_argument("--headless=new")
# # # #     chrome_options.add_argument("--disable-gpu")
# # # #     chrome_options.add_argument("--no-sandbox")

# # # #     service = Service(chromedriver_path)
# # # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # # #     driver.get(url)
# # # #     time.sleep(5)

# # # #     chat = []
# # # #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# # # #     for container in containers:
# # # #         role = container.get_attribute("data-message-author-role")
# # # #         try:
# # # #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# # # #             message_text = message_elem.text.strip()
# # # #         except:
# # # #             message_text = container.text.strip()

# # # #         if message_text:
# # # #             if role == "user":
# # # #                 chat.append(("User", message_text))
# # # #             elif role == "assistant":
# # # #                 chat.append(("ChatGPT", message_text))

# # # #     driver.quit()
# # # #     return chat

# # # # # PDF Generator Class
# # # # class ChatPDF(FPDF):
# # # #     def header(self):
# # # #         self.set_font("Arial", 'B', 14)
# # # #         self.cell(0, 10, "ChatGPT Conversation", align="C")
# # # #         self.ln(10)

# # # #     def add_message(self, speaker, message):
# # # #         self.set_font("Arial", "B", 12)
# # # #         self.set_text_color(0)
# # # #         self.multi_cell(0, 8, f"{speaker}:", align="L")
# # # #         self.ln(1)

# # # #         self.set_font("Arial", "", 12)
# # # #         lines = message.split('\n')
# # # #         in_code_block = False
# # # #         y_start = None

# # # #         for line in lines:
# # # #             stripped = line.strip()

# # # #             # Start or end of code block
# # # #             if stripped.startswith("```"):
# # # #                 in_code_block = not in_code_block
# # # #                 if in_code_block:
# # # #                     y_start = self.get_y()
# # # #                 else:
# # # #                     y_end = self.get_y()
# # # #                     self.set_draw_color(180, 180, 180)
# # # #                     self.rect(x=10, y=y_start - 1, w=190, h=y_end - y_start + 2)
# # # #                     self.ln(2)
# # # #                 continue

# # # #             if in_code_block:
# # # #                 self.set_font("Courier", "", 11)
# # # #                 self.set_fill_color(245, 245, 245)
# # # #                 self.multi_cell(0, 6, line)
# # # #                 self.set_font("Arial", "", 12)
# # # #             elif stripped.startswith("- ") or stripped.startswith("•"):
# # # #                 self.cell(5)
# # # #                 self.multi_cell(0, 6, u"\u2022 " + stripped[2:])
# # # #             elif any(stripped.startswith(f"{n}. ") for n in range(1, 10)):
# # # #                 self.multi_cell(0, 6, stripped)
# # # #             else:
# # # #                 self.multi_cell(0, 6, line)

# # # #         self.ln(4)

# # # # # Button to run everything
# # # # if st.button("Fetch & Export"):
# # # #     if url:
# # # #         try:
# # # #             with st.spinner("Fetching and formatting chat..."):
# # # #                 chat = fetch_chat_with_selenium(url)

# # # #                 # Show in Streamlit
# # # #                 for speaker, message in chat:
# # # #                     emoji = "🧑" if speaker == "User" else "🤖"
# # # #                     st.markdown(f"**{emoji} {speaker}**:\n{message}\n---")

# # # #                 # Create PDF
# # # #                 pdf = ChatPDF()
# # # #                 pdf.add_page()
# # # #                 pdf.set_auto_page_break(auto=True, margin=15)

# # # #                 for speaker, message in chat:
# # # #                     clean_text = remove_emojis(message)
# # # #                     pdf.add_message(speaker, clean_text)

# # # #                 pdf_path = "chatgpt_chat.pdf"
# # # #                 pdf.output(pdf_path)

# # # #                 with open(pdf_path, "rb") as f:
# # # #                     st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

# # # #         except Exception as e:
# # # #             st.error(f"❌ Error: {e}")

# # # import streamlit as st
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.chrome.options import Options
# # # from selenium.webdriver.common.by import By
# # # from jinja2 import Environment, FileSystemLoader
# # # import pdfkit
# # # import time
# # # import os

# # # st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# # # st.title("📄 Export ChatGPT Chat to Styled PDF")

# # # # 🔧 CONFIG: Set your paths here
# # # chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # Change to your path
# # # wkhtmltopdf_path = r"C:\Users\shrik\Downloads\wkhtmltopdf\bin\wkhtmltopdf.exe"     # Change to your wkhtmltopdf path

# # # config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# # # url = st.text_input("Paste your ChatGPT shared link:")

# # # def fetch_chat_with_selenium(url):
# # #     chrome_options = Options()
# # #     chrome_options.add_argument("--headless=new")
# # #     chrome_options.add_argument("--disable-gpu")
# # #     chrome_options.add_argument("--no-sandbox")

# # #     service = Service(chromedriver_path)
# # #     driver = webdriver.Chrome(service=service, options=chrome_options)
# # #     driver.get(url)
# # #     time.sleep(5)

# # #     chat = []
# # #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# # #     for container in containers:
# # #         role = container.get_attribute("data-message-author-role")
# # #         try:
# # #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# # #             message_html = message_elem.get_attribute("innerHTML").strip()

# # #         except:
# # #             message_text = container.text.strip()

# # #         if message_text:
# # #             speaker = "User" if role == "user" else "ChatGPT"
# # #             chat.append((speaker, message_text))

# # #     driver.quit()
# # #     return chat

# # # def generate_html(chat):
# # #     env = Environment(loader=FileSystemLoader("templates"))
# # #     template = env.get_template("chat_template.html")
# # #     return template.render(chat=chat)

# # # if st.button("Fetch & Export to PDF"):
# # #     if url:
# # #         try:
# # #             with st.spinner("Fetching chat..."):
# # #                 chat = fetch_chat_with_selenium(url)

# # #             # Render HTML
# # #             html_content = generate_html(chat)
# # #             with open("chat_output.html", "w", encoding="utf-8") as f:
# # #                 f.write(html_content)

# # #             # Convert to PDF
# # #             pdfkit.from_file("chat_output.html", "chat_output.pdf", configuration=config)

# # #             # Display and download
# # #             st.success("✅ PDF generated successfully!")
# # #             with open("chat_output.pdf", "rb") as f:
# # #                 st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

# # #         except Exception as e:
# # #             st.error(f"❌ Error: {e}")

# # def fetch_chat_with_selenium(url):
# #     chrome_options = Options()
# #     chrome_options.add_argument("--headless=new")
# #     chrome_options.add_argument("--disable-gpu")
# #     chrome_options.add_argument("--no-sandbox")

# #     service = Service(chromedriver_path)
# #     driver = webdriver.Chrome(service=service, options=chrome_options)
# #     driver.get(url)
# #     time.sleep(5)

# #     chat = []
# #     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

# #     for container in containers:
# #         role = container.get_attribute("data-message-author-role")
# #         try:
# #             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
# #             message_html = message_elem.get_attribute("innerHTML").strip()
# #         except:
# #             message_html = container.text.strip()

# #         if message_html:
# #             if role == "user":
# #                 chat.append(("User", message_html))
# #             elif role == "assistant":
# #                 chat.append(("ChatGPT", message_html))
# #             else:
# #                 # skip unknown roles
# #                 pass

# #     driver.quit()
# #     return chat


# import streamlit as st
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from jinja2 import Environment, FileSystemLoader
# import pdfkit
# import time
# import os

# # ------------- CONFIG -------------
# chromedriver_path = r"C:\chromedriver\chromedriver-win64\chromedriver.exe"  # <-- Update this
# wkhtmltopdf_path = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"      # <-- Update this

# pdfkit_config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)

# # Streamlit UI
# st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
# st.title("📄 Export ChatGPT Shared Chat to PDF")

# url = st.text_input("Paste your ChatGPT shared chat link:")

# def fetch_chat_with_selenium(url):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--no-sandbox")

#     service = Service(chromedriver_path)
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     driver.get(url)
#     time.sleep(5)  # Wait for page JS to load

#     chat = []
#     # Each message container has 'data-message-author-role' attribute
#     containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')
    
#     for container in containers:
#         role = container.get_attribute("data-message-author-role")
#         try:
#             message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
#             message_html = message_elem.get_attribute("innerHTML").strip()
#         except Exception:
#             # fallback to text if markdown not found
#             message_html = container.text.strip()

#         if message_html:
#             if role == "user":
#                 chat.append(("User", message_html))
#             elif role == "assistant":
#                 chat.append(("ChatGPT", message_html))
#             else:
#                 # Ignore other roles if any
#                 pass
    
#     driver.quit()
#     return chat

# def render_html(chat):
#     env = Environment(loader=FileSystemLoader("templates"))
#     template = env.get_template("chat_template.html")
#     return template.render(chat=chat)

# if st.button("Fetch & Export to PDF"):
#     if url:
#         try:
#             with st.spinner("Fetching chat..."):
#                 chat = fetch_chat_with_selenium(url)

#             # Generate HTML from template
#             html_content = render_html(chat)
#             with open("chat_output.html", "w", encoding="utf-8") as f:
#                 f.write(html_content)

#             # Generate PDF from HTML
#             pdfkit.from_file("chat_output.html", "chat_output.pdf", configuration=pdfkit_config)

#             st.success("✅ PDF generated successfully!")
#             with open("chat_output.pdf", "rb") as f:
#                 st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fpdf import FPDF
from bs4 import BeautifulSoup
import time

# Set Streamlit page config
st.set_page_config(page_title="ChatGPT Chat Exporter", page_icon="💬")
st.title("📄 Export ChatGPT Shared Chat to PDF")

# Input field for ChatGPT shared URL
url = st.text_input("Paste your ChatGPT shared chat link:")

# Selenium setup (Streamlit Cloud handles this automatically if you add requirements properly)
def fetch_chat_with_selenium(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    # Automatically find ChromeDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Wait for content to load

    chat = []
    containers = driver.find_elements(By.CSS_SELECTOR, '[data-message-author-role]')

    for container in containers:
        role = container.get_attribute("data-message-author-role")
        try:
            message_elem = container.find_element(By.CSS_SELECTOR, 'div.markdown')
            message_html = message_elem.get_attribute("innerHTML").strip()
        except:
            message_html = container.text.strip()

        if message_html:
            speaker = "User" if role == "user" else "ChatGPT"
            chat.append((speaker, message_html))

    driver.quit()
    return chat

# PDF builder using FPDF
class ChatPDF(FPDF):
    def header(self):
        self.set_font("Arial", 'B', 14)
        self.cell(0, 10, "ChatGPT Conversation", ln=True, align="C")
        self.ln(5)

    def add_message(self, speaker, html_content):
        self.set_font("Arial", 'B', 12)
        self.cell(0, 10, f"{speaker}:", ln=True)
        self.set_font("Arial", '', 12)

        # Convert HTML to plain text
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()
        self.multi_cell(0, 8, text)
        self.ln(3)

# Button to run everything
if st.button("Fetch & Export to PDF"):
    if url:
        try:
            with st.spinner("Fetching chat..."):
                chat = fetch_chat_with_selenium(url)

            # Show chat on Streamlit
            for speaker, html in chat:
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text()
                emoji = "🧑" if speaker == "User" else "🤖"
                st.markdown(f"**{emoji} {speaker}**:\n{text}\n---")

            # Generate PDF
            pdf = ChatPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)

            for speaker, html in chat:
                pdf.add_message(speaker, html)

            pdf_path = "chatgpt_chat.pdf"
            pdf.output(pdf_path)

            with open(pdf_path, "rb") as f:
                st.download_button("📥 Download PDF", f, file_name="chatgpt_chat.pdf")

        except Exception as e:
            st.error(f"❌ Error: {e}")
