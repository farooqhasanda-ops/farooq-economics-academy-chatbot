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

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbw9k0DtyF4Rqg7Wcouu-yIrTe4luFYw77_SjnoQthrp-3Sm6mDKe1PsGtmoGJcDMqXl/exec"


def make_whatsapp_link(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


# =========================
# SMART COUNSELLOR CHATBOT
# =========================
def chatbot(message, history):
    user_msg = message.lower().strip()

    if any(word in user_msg for word in ["hi", "hello", "assalam", "salam", "hey"]):
        return f"""Assalamu Alaikum / Hello 👋

Welcome to **{ACADEMY_NAME}** 🎓

I am here to guide students and parents for Intermediate 1st & 2nd Year tuition.

📚 Subjects:
- Civics
- Economics
- Commerce
- Accountancy

🖥 Modes:
- Online tuition
- Offline tuition
- Home tuition available

You can ask about admission, fees, demo class, subjects, timings, or fill the enquiry form below."""

    elif any(word in user_msg for word in ["admission", "join", "register", "enquiry", "enroll", "enrol"]):
        return f"""📌 **Admissions are open!**

At **{ACADEMY_NAME}**, we focus on concept clarity, regular guidance, and exam preparation.

Please fill the enquiry form below or WhatsApp us directly.

📞 Contact / WhatsApp: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["fee", "fees", "price", "cost", "charges"]):
        return f"""💰 **Fee Details**

📘 Intermediate 1st Year: ₹6,000  
📗 Intermediate 2nd Year: ₹8,000  
📚 Per Subject: ₹6,000  

Special Discount:
If a student takes all 3 subjects, total fee will be **₹10,000** instead of ₹12,000.

Monthly option: ₹7,000

For final confirmation and discount details, please contact:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["subject", "subjects", "course", "courses"]):
        return """📚 **Subjects Offered**

We provide tuition for:

- Civics
- Economics
- Commerce
- Accountancy

Available for Intermediate 1st Year and 2nd Year students."""

    elif any(word in user_msg for word in ["online", "offline", "mode", "home tuition", "home"]):
        return f"""🖥️🏫 **Tuition Modes Available**

We offer:
- Online tuition
- Offline tuition
- Home tuition

Please share your area/location so we can guide you properly.

📞 Contact: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["demo", "trial", "sample"]):
        return f"""✅ **Demo Class Available**

Yes, demo class is available.

Please share:
1. Student Name
2. Class
3. Subject
4. Area
5. Phone Number

Or contact directly:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["timing", "time", "batch"]):
        return f"""⏰ **Class Timings**

Current batch timings:
**{TIMINGS}**

For exact subject-wise timing, please contact:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["location", "address", "where"]):
        return f"""📍 **Location**

{ACADEMY_NAME}  
{LOCATION}

Online, Offline and Home Tuition are available.

📞 Contact: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["why join", "why should", "benefit", "better", "special"]):
        return f"""🌟 **Why Choose {ACADEMY_NAME}?**

Every student needs proper guidance, personal attention, and clear understanding of concepts.

At **{ACADEMY_NAME}**, we focus on:
✅ Concept clarity  
✅ Exam-oriented preparation  
✅ Personal attention  
✅ Doubt clarification  
✅ Regular guidance  
✅ Online, offline and home tuition options  
✅ Student-friendly teaching in English  

Our aim is not only to complete the syllabus, but to build confidence in the student.

📞 For admission guidance: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["weak", "slow", "doubt", "not understanding", "poor"]):
        return f"""Don’t worry 😊

We give proper attention to students who are weak in basics or facing difficulty in understanding subjects.

We focus on:
✅ Basic concepts  
✅ Step-by-step explanation  
✅ Doubt clearing  
✅ Exam preparation  
✅ Confidence building  

Please fill the enquiry form or contact:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["contact", "phone", "mobile", "call", "number", "whatsapp"]):
        msg = "Assalamu Alaikum, I want admission details from Farooq Economics Academy."
        return f"""📞 **Contact Details**

Phone / WhatsApp: **{CONTACT_NUMBER}**  
Email: **{EMAIL}**  
Location: **{LOCATION}**

💬 WhatsApp directly:
👉 {make_whatsapp_link(msg)}"""

    else:
        return f"""Thank you for your message 😊

I can help you with:
- Admission
- Fees
- Subjects
- Demo class
- Online / Offline / Home tuition
- Timings
- Location
- Parent guidance

For quick help, WhatsApp:
📞 **{CONTACT_NUMBER}**"""


# =========================
# SAVE FORM TO GOOGLE SHEET + WHATSAPP
# =========================
def submit_form(name, parent_name, phone, student_class, subject, mode, area, preferred_timing, message):
    if not name or not phone:
        return "❌ Please enter Student Name and Mobile Number."

    data = {
        "name": name,
        "parent_name": parent_name,
        "phone": phone,
        "student_class": student_class,
        "subject": subject,
        "mode": mode,
        "area": area,
        "preferred_timing": preferred_timing,
        "message": message
    }

    try:
        response = requests.post(GOOGLE_SHEET_URL, json=data, timeout=10)
        if response.status_code not in [200, 302]:
            return f"❌ Enquiry could not be saved. Error code: {response.status_code}"
    except Exception:
        return "❌ Internet/server error. Please try again."

    whatsapp_message = (
        f"Assalamu Alaikum, I want admission details from Farooq Economics Academy.\n"
        f"Student Name: {name}\n"
        f"Parent Name: {parent_name}\n"
        f"Mobile Number: {phone}\n"
        f"Class: {student_class}\n"
        f"Subject: {subject}\n"
        f"Mode: {mode}\n"
        f"Area / Location: {area}\n"
        f"Preferred Timing: {preferred_timing}\n"
        f"Message: {message}"
    )

    wa_link = make_whatsapp_link(whatsapp_message)

    return f"""✅ **Your enquiry has been saved successfully.**

Now click below to send it on WhatsApp:

👉 {wa_link}
"""


# =========================
# QUICK BUTTONS
# =========================
def quick_admission():
    return "Admissions are open for Intermediate 1st & 2nd Year students. Please fill the enquiry form below."

def quick_fees():
    return "Fees: 1st Year ₹6,000 | 2nd Year ₹8,000 | Per Subject ₹6,000 | 3 Subjects ₹10,000 discount offer."

def quick_subjects():
    return "Subjects: Civics, Economics, Commerce, Accountancy."

def quick_contact():
    return f"Contact / WhatsApp: {CONTACT_NUMBER}"


# =========================
# USER INTERFACE
# =========================
with gr.Blocks(title="Farooq Economics Academy") as demo:

    gr.Markdown(f"""
# 🎓 {ACADEMY_NAME}

### Intermediate 1st Year & 2nd Year Tuition  
**Subjects:** Civics | Economics | Commerce | Accountancy  
**Mode:** Online | Offline | Home Tuition  
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

    gr.Markdown("## 🤖 Smart Academy Counsellor")

    gr.ChatInterface(
        fn=chatbot,
        title="Farooq Economics Academy AI Assistant",
        description="Ask about admissions, fees, demo class, subjects, home tuition, online/offline tuition, and parent guidance."
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
        parent_name = gr.Textbox(label="Parent Name")

    with gr.Row():
        phone = gr.Textbox(label="Mobile Number")
        area = gr.Textbox(label="Area / Location")

    with gr.Row():
        student_class = gr.Dropdown(
            choices=["Intermediate 1st Year", "Intermediate 2nd Year"],
            label="Class",
            value="Intermediate 1st Year"
        )

        subject = gr.Dropdown(
            choices=["Civics", "Economics", "Commerce", "Accountancy", "All Subjects"],
            label="Subject",
            value="Economics"
        )

    with gr.Row():
        mode = gr.Radio(
            choices=["Online", "Offline", "Home Tuition"],
            label="Mode of Tuition",
            value="Offline"
        )

        preferred_timing = gr.Dropdown(
            choices=["Morning", "Afternoon", "Evening", "Night", "Flexible"],
            label="Preferred Timing",
            value="Evening"
        )

    message = gr.Textbox(
        label="Message / Doubt",
        placeholder="Example: I want Economics tuition for Intermediate 1st Year.",
        lines=3
    )

    submit_btn = gr.Button("Submit Enquiry")
    form_output = gr.Markdown()

    submit_btn.click(
        fn=submit_form,
        inputs=[name, parent_name, phone, student_class, subject, mode, area, preferred_timing, message],
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


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
