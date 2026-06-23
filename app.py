import gradio as gr
from urllib.parse import quote

# =========================
# ACADEMY DETAILS
# =========================
ACADEMY_NAME = "Farooq Economics Academy"
CONTACT_NUMBER = "9989221983"
WHATSAPP_NUMBER = "919989221983"   # 91 + your mobile number without +
EMAIL = "frkfarooqhasan@gmail.com"
LOCATION = "Tolichowki, Hyderabad"
TIMINGS = "5:00 PM to 11:00 PM"

SUBJECTS = [
    "Economics",
    "Commerce",
    "Civics",
    "Accountancy"
]

CLASSES = [
    "Intermediate 1st Year",
    "Intermediate 2nd Year"
]

# =========================
# HELPER: CREATE WHATSAPP LINK
# =========================
def make_whatsapp_link(message: str):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

# =========================
# SMART CHATBOT FUNCTION
# =========================
def chatbot(message, history):
    user_msg = message.strip().lower()

    greeting_keywords = ["hi", "hello", "assalamu", "assalamualaikum", "salam", "hey"]
    fee_keywords = ["fee", "fees", "price", "charges", "cost"]
    admission_keywords = ["admission", "join", "register", "enroll", "enrol", "seat"]
    contact_keywords = ["contact", "phone", "number", "mobile", "call"]
    whatsapp_keywords = ["whatsapp", "watsup", "wa"]
    location_keywords = ["location", "address", "where", "academy location", "place"]
    subject_keywords = ["subject", "subjects", "course", "courses", "what do you teach"]
    class_keywords = ["1st year", "first year", "2nd year", "second year", "intermediate"]
    online_keywords = ["online", "offline", "mode", "home tuition"]
    timing_keywords = ["timing", "timings", "time", "class timing", "class timings"]
    demo_keywords = ["demo", "trial", "sample class"]
    teacher_keywords = ["who teaches", "sir", "faculty", "teacher"]

    # 1) Greeting
    if any(word in user_msg for word in greeting_keywords):
        return f"""Assalamu Alaikum / Hello 👋

Welcome to **{ACADEMY_NAME}** 🎓

I’m here to help you with:
- Admissions
- Subjects offered
- Online / Offline tuition
- Fee enquiry
- Contact details
- Timings

Please tell me how I can help you today."""

    # 2) Admission
    elif any(word in user_msg for word in admission_keywords):
        return f"""📌 **Admissions are open at {ACADEMY_NAME}!**

We provide tuition for:
- **Intermediate 1st Year**
- **Intermediate 2nd Year**

📚 **Subjects Offered**
- Economics
- Commerce
- Civics
- Accountancy

🖥 **Modes Available**
- Online Tuition
- Offline Tuition

To guide you properly, please share these details:
1. Student Name  
2. Class (1st Year / 2nd Year)  
3. Subject  
4. Mode (Online / Offline)  
5. Area / Location  
6. Phone Number  

Or contact / WhatsApp directly on **{CONTACT_NUMBER}**."""

    # 3) Fees
    elif any(word in user_msg for word in fee_keywords):
        return f"""💰 **Fee Details**

Fees depend on:
- Class
- Subject
- Mode (Online / Offline)

For exact fee details, please share:
1. Student class
2. Subject needed
3. Online or Offline

📞 Contact / WhatsApp: **{CONTACT_NUMBER}**"""

    # 4) Contact
    elif any(word in user_msg for word in contact_keywords):
        return f"""📞 **Contact Details**

**{ACADEMY_NAME}**  
Phone / WhatsApp: **{CONTACT_NUMBER}**  
Email: **{EMAIL}**

You may contact us for:
- Admission enquiry
- Fee details
- Subject guidance
- Online / Offline tuition"""

    # 5) WhatsApp
    elif any(word in user_msg for word in whatsapp_keywords):
        wa_msg = "Assalamu Alaikum, I want details about admission in Farooq Economics Academy."
        wa_link = make_whatsapp_link(wa_msg)
        return f"""💬 **WhatsApp Enquiry**

Please click the link below to chat directly on WhatsApp:

👉 {wa_link}

Or save this number and message us:
**{CONTACT_NUMBER}**"""

    # 6) Location
    elif any(word in user_msg for word in location_keywords):
        return f"""📍 **Academy Location**

**{ACADEMY_NAME}**  
Location: **{LOCATION}**

For exact directions or admission help, please contact:
📞 **{CONTACT_NUMBER}**"""

    # 7) Subjects / Courses
    elif any(word in user_msg for word in subject_keywords):
        return f"""📚 **Subjects Offered at {ACADEMY_NAME}**

We teach:
- Economics
- Commerce
- Civics
- Accountancy

Available for:
- **Intermediate 1st Year**
- **Intermediate 2nd Year**

If you want subject-wise guidance, tell me:
- Your class
- Your subject
- Online or Offline preference"""

    # 8) Classes
    elif any(word in user_msg for word in class_keywords):
        return f"""🎓 **Classes Available**

We provide tuition for:
- **Intermediate 1st Year**
- **Intermediate 2nd Year**

Subjects include:
- Economics
- Commerce
- Civics
- Accountancy

Please tell me which class and subject you need help with."""

    # 9) Online / Offline / Home tuition
    elif any(word in user_msg for word in online_keywords):
        return f"""🖥🏫 **Tuition Modes Available**

At **{ACADEMY_NAME}**, we offer:
- **Online Tuition**
- **Offline Tuition**

If needed, you can contact us to discuss the best option for your child / yourself.

📞 Contact / WhatsApp: **{CONTACT_NUMBER}**"""

    # 10) Timings
    elif any(word in user_msg for word in timing_keywords):
        return f"""⏰ **Academy Timings**

Current class timings: **{TIMINGS}**

For exact batch timing according to class and subject, please contact:
📞 **{CONTACT_NUMBER}**"""

    # 11) Demo class
    elif any(word in user_msg for word in demo_keywords):
        return f"""📘 **Demo / Guidance Class**

For demo class or admission guidance, please contact directly on:
📞 **{CONTACT_NUMBER}**

Please mention:
- Student Name
- Class
- Subject
- Online / Offline preference"""

    # 12) Teacher / faculty
    elif any(word in user_msg for word in teacher_keywords):
        return f"""👨‍🏫 **About the Academy**

At **{ACADEMY_NAME}**, students are guided with personal attention, subject clarity and exam-focused teaching for Intermediate students.

For admission or class details, please contact:
📞 **{CONTACT_NUMBER}**"""

    # 13) Fallback answer
    else:
        return f"""Thank you for your message. 😊

I can help you with:
- **Admission enquiry**
- **Fee details**
- **Subjects offered**
- **Online / Offline tuition**
- **Contact details**
- **Academy location**
- **Class timings**

Please type one of these:
- Admission
- Fees
- Subjects
- Contact
- Location
- Online / Offline

Or directly WhatsApp / call us on **{CONTACT_NUMBER}**."""

# =========================
# ADMISSION FORM SUBMIT FUNCTION
# =========================
def submit_form(name, phone, student_class, subject, mode):
    if not name.strip() or not phone.strip():
        return "❌ Please enter Student Name and Mobile Number."

    msg = (
        f"Assalamu Alaikum, I want admission details from Farooq Economics Academy.%0A"
        f"Student Name: {name}%0A"
        f"Mobile Number: {phone}%0A"
        f"Class: {student_class}%0A"
        f"Subject: {subject}%0A"
        f"Mode: {mode}"
    )

    wa_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg}"

    return f"""✅ **Your enquiry is ready.**

Please click the WhatsApp link below to send your admission enquiry:

👉 {wa_link}
"""

# =========================
# QUICK BUTTON ACTIONS
# =========================
def quick_admission():
    return """Admissions are open for Intermediate 1st Year and 2nd Year students.

Please share:
1. Student Name
2. Class
3. Subject
4. Online / Offline
5. Phone Number"""

def quick_fees():
    return f"""Fees depend on class, subject and mode.
Please contact / WhatsApp on **{CONTACT_NUMBER}** for exact fee details."""

def quick_subjects():
    return """Subjects offered:
- Economics
- Commerce
- Civics
- Accountancy

Available for Intermediate 1st Year and 2nd Year students."""

def quick_contact():
    return f"""Contact Farooq Economics Academy:
📞 {CONTACT_NUMBER}
📧 {EMAIL}
📍 {LOCATION}"""

# =========================
# UI
# =========================
with gr.Blocks(title="Farooq Economics Academy") as demo:
    gr.Markdown(
        f"""
# 🎓 {ACADEMY_NAME}

### Intermediate 1st Year & 2nd Year Tuition  
**Subjects:** Economics | Commerce | Civics | Accountancy  
**Mode:** Online & Offline  
**Contact:** {CONTACT_NUMBER}

---
"""
    )

    with gr.Row():
        gr.HTML(
            f"""
            <a href="tel:{CONTACT_NUMBER}" target="_blank">
                <button style="padding:10px 20px; font-size:16px; cursor:pointer;">📞 Call Now</button>
            </a>
            """
        )

        gr.HTML(
            f"""
            <a href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">
                <button style="padding:10px 20px; font-size:16px; cursor:pointer;">💬 WhatsApp Now</button>
            </a>
            """
        )

    gr.Markdown("## 🤖 Chat with Academy Assistant")
    chatbot_ui = gr.ChatInterface(
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
            label="Class"
        )
        subject = gr.Dropdown(
            choices=["Economics", "Commerce", "Civics", "Accountancy"],
            label="Subject"
        )

    mode = gr.Radio(
        choices=["Online", "Offline"],
        label="Mode of Tuition"
    )

    submit_btn = gr.Button("Submit Enquiry")
    form_output = gr.Markdown()

    submit_btn.click(
        fn=submit_form,
        inputs=[name, phone, student_class, subject, mode],
        outputs=form_output
    )

    gr.Markdown(
        f"""
---
### 📍 Academy Details
**Academy Name:** {ACADEMY_NAME}  
**Location:** {LOCATION}  
**Timings:** {TIMINGS}  
**Contact:** {CONTACT_NUMBER}  
**Email:** {EMAIL}
"""
    )

# =========================
# RUN APP
# =========================
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
