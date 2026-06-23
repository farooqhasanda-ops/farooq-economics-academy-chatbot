import gradio as gr
from urllib.parse import quote
import requests

# =========================
# ACADEMY DETAILS
# =========================
ACADEMY_NAME = "Farooq Economics Academy"
CONTACT_NUMBER = "9989221983"
WHATSAPP_NUMBER = "919989221983"
EMAIL = "frkfarooqhasan@gmail.com"
LOCATION = "Tolichowki, Hyderabad"
TIMINGS = "5:00 PM to 11:00 PM"

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbxETmWa0y6Be3dqSDOeXb-pDdZm18IWPGGvi6ThhPqXk4_0naZHUpsAZrFWF2lCmq_Ghw/exec"

# =========================
# WHATSAPP LINK
# =========================
def make_whatsapp_link(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

# =========================
# SMART CHATBOT
# =========================
def chatbot(message, history):
    user_msg = message.lower().strip()

    if any(word in user_msg for word in ["hi", "hello", "assalam", "salam", "hey"]):
        return f"""Assalamu Alaikum / Hello 👋

Welcome to **{ACADEMY_NAME}** 🎓

We provide tuition for Intermediate 1st Year and 2nd Year students.

Subjects:
- Economics
- Commerce
- Civics
- Accountancy

You can ask me about admissions, fees, subjects, timings, online/offline tuition, or contact details."""

    elif any(word in user_msg for word in ["admission", "join", "register", "enquiry", "enroll", "enrol"]):
        return f"""📌 **Admissions are open!**

Please share:
1. Student Name
2. Class
3. Subject
4. Online or Offline
5. Phone Number

Or WhatsApp directly: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["fee", "fees", "price", "cost", "charges"]):
        return f"""💰 **Fee Details**

Fees depend on:
- Class
- Subject
- Online / Offline mode

For exact fee details, please contact / WhatsApp:
**{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["subject", "subjects", "course", "courses"]):
        return """📚 **Subjects Offered**

- Economics
- Commerce
- Civics
- Accountancy

Available for Intermediate 1st Year and 2nd Year students."""

    elif any(word in user_msg for word in ["online", "offline", "mode", "home tuition"]):
        return """🖥️🏫 **Tuition Mode**

Both **Online** and **Offline** tuition are available."""

    elif any(word in user_msg for word in ["timing", "time", "batch"]):
        return f"""⏰ **Timings**

Current timing: **{TIMINGS}**

For exact batch timing, please contact:
**{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["location", "address", "where"]):
        return f"""📍 **Location**

{ACADEMY_NAME}  
{LOCATION}

Contact: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["contact", "phone", "mobile", "call", "number"]):
        return f"""📞 **Contact Details**

Phone / WhatsApp: **{CONTACT_NUMBER}**  
Email: **{EMAIL}**  
Location: **{LOCATION}**"""

    elif any(word in user_msg for word in ["whatsapp", "watsup", "wa"]):
        msg = "Assalamu Alaikum, I want admission details from Farooq Economics Academy."
        return f"""💬 Click here to WhatsApp:

👉 {make_whatsapp_link(msg)}"""

    else:
        return f"""Thank you for your message 😊

I can help you with:
- Admission
- Fees
- Subjects
- Online / Offline tuition
- Timings
- Location
- Contact details

For quick help, WhatsApp: **{CONTACT_NUMBER}**"""

# =========================
# SAVE ENQUIRY TO GOOGLE SHEET + WHATSAPP
# =========================
def submit_form(name, phone, student_class, subject, mode):
    if not name or not phone:
        return "❌ Please enter Student Name and Mobile Number."

    data = {
        "name": name,
        "phone": phone,
        "student_class": student_class,
        "subject": subject,
        "mode": mode
    }

    try:
        response = requests.post(GOOGLE_SHEET_URL, json=data, timeout=10)
        if response.status_code != 200:
            return "❌ Enquiry could not be saved. Please try again."
    except Exception:
        return "❌ Internet/server error. Please try again."

    whatsapp_message = (
        f"Assalamu Alaikum, I want admission details from Farooq Economics Academy.\n"
        f"Student Name: {name}\n"
        f"Mobile Number: {phone}\n"
        f"Class: {student_class}\n"
        f"Subject: {subject}\n"
        f"Mode: {mode}"
    )

    wa_link = make_whatsapp_link(whatsapp_message)

    return f"""✅ **Your enquiry has been saved successfully in Google Sheet.**

Now click below to send it on WhatsApp:

👉 {wa_link}
"""

# =========================
# QUICK BUTTONS
# =========================
def quick_admission():
    return "Admissions are open for Intermediate 1st Year and 2nd Year students."

def quick_fees():
    return f"Fees depend on class, subject and mode. Contact: {CONTACT_NUMBER}"

def quick_subjects():
    return "Subjects: Economics, Commerce, Civics, Accountancy"

def quick_contact():
    return f"Contact / WhatsApp: {CONTACT_NUMBER}"

# =========================
# USER INTERFACE
# =========================
with gr.Blocks(title="Farooq Economics Academy") as demo:

    gr.Markdown(f"""
# 🎓 {ACADEMY_NAME}

### Intermediate 1st Year & 2nd Year Tuition  
**Subjects:** Economics | Commerce | Civics | Accountancy  
**Mode:** Online & Offline  
**Contact:** {CONTACT_NUMBER}

---
""")

    with gr.Row():
        gr.HTML(f"""
        <a href="tel:{CONTACT_NUMBER}" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">📞 Call Now</button>
        </a>
        """)

        gr.HTML(f"""
        <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">
        <button style="padding:10px 20px; font-size:16px;">💬 WhatsApp Now</button>
        </a>
        """)

    gr.Markdown("## 🤖 Chat with Academy Assistant")

    gr.ChatInterface(
        fn=chatbot,
        title="Farooq Economics Academy AI Assistant",
        description="Ask about admissions, fees, subjects, timings, online/offline tuition, and contact details."
    )

    gr.Markdown("## ⚡ Quick Information")

    with gr.Row():
        btn_admission = gr.Button("📝 Admission Info")
        btn_fees = gr.Button("💰 Fee Info")
        btn_subjects = gr.Button("📚 Subjects")
        btn_contact = gr.Button("📞 Contact")

    quick_output = gr.Markdown()

    btn_admission.click(fn=quick_admission, outputs=quick_output)
    btn_fees.click(fn=quick_fees, outputs=quick_output)
    btn_subjects.click(fn=quick_subjects, outputs=quick_output)
    btn_contact.click(fn=quick_contact, outputs=quick_output)

    gr.Markdown("## 📝 Admission Enquiry Form")

    with gr.Row():
        name = gr.Textbox(label="Student Name")
        phone = gr.Textbox(label="Mobile Number")

    with gr.Row():
        student_class = gr.Dropdown(
            choices=["Intermediate 1st Year", "Intermediate 2nd Year"],
            label="Class",
            value="Intermediate 1st Year"
        )

        subject = gr.Dropdown(
            choices=["Economics", "Commerce", "Civics", "Accountancy"],
            label="Subject",
            value="Economics"
        )

    mode = gr.Radio(
        choices=["Online", "Offline"],
        label="Mode of Tuition",
        value="Offline"
    )

    submit_btn = gr.Button("Submit Enquiry")
    form_output = gr.Markdown()

    submit_btn.click(
        fn=submit_form,
        inputs=[name, phone, student_class, subject, mode],
        outputs=form_output
    )

    gr.Markdown(f"""
---
### 📍 Academy Details

**Academy Name:** {ACADEMY_NAME}  
**Location:** {LOCATION}  
**Timings:** {TIMINGS}  
**Contact:** {CONTACT_NUMBER}  
**Email:** {EMAIL}
""")

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
