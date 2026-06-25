import gradio as gr
from urllib.parse import quote
import requests

ACADEMY_NAME = "Farooq Economics Academy"
CONTACT_NUMBER = "9989221983"
WHATSAPP_NUMBER = "919989221983"
EMAIL = "frkfarooqhasan@gmail.com"
LOCATION = "Tolichowki, Hyderabad"
TIMINGS = "5:00 PM to 11:00 PM"

GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbw9k0DtyF4Rqg7Wcouu-yIrTe4luFYw77_SjnoQthrp-3Sm6mDKe1PsGtmoGJcDMqXl/exec"


def make_whatsapp_link(message):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def chatbot(message, history):
    user_msg = message.lower().strip()

    if any(word in user_msg for word in ["hi", "hello", "assalam", "salam", "hey"]):
        return f"""Assalamu Alaikum / Hello 👋

Welcome to **{ACADEMY_NAME}** 🎓

We guide Intermediate 1st & 2nd Year students with personal attention and exam-focused teaching.

📚 Subjects: Civics, Economics, Commerce, Accountancy  
🖥 Mode: Online, Offline & Home Tuition  
✅ Demo Class Available  

How can I help you today?"""

    elif any(word in user_msg for word in ["fee", "fees", "price", "cost", "charges"]):
        return """💰 **Fee Details**

📘 1st Year: ₹6,000  
📗 2nd Year: ₹8,000  
📚 Per Subject: ₹6,000  
🎁 All 3 Subjects: ₹10,000 only  

For confirmation, please contact: **9989221983**"""

    elif any(word in user_msg for word in ["admission", "join", "register", "enquiry", "enroll", "enrol"]):
        return f"""📌 **Admissions are open!**

Please fill the enquiry form below or WhatsApp us directly.

We will guide you according to your class, subject and timing.

📞 Contact / WhatsApp: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["demo", "trial", "sample"]):
        return f"""✅ **Demo Class Available**

Please share student name, class, subject and area.

Or contact directly:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["why join", "why should", "benefit", "better", "special", "weak", "doubt"]):
        return f"""🌟 **Why Choose {ACADEMY_NAME}?**

✅ Personal attention  
✅ Concept clarity  
✅ Doubt clearing  
✅ Exam-focused preparation  
✅ Parent guidance  
✅ Online, offline and home tuition  

Our aim is to build confidence and improve academic performance.

📞 Admission guidance: **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["subject", "subjects", "course", "courses"]):
        return """📚 **Subjects Offered**

- Civics
- Economics
- Commerce
- Accountancy

Available for Intermediate 1st Year and 2nd Year."""

    elif any(word in user_msg for word in ["online", "offline", "home tuition", "home"]):
        return f"""🖥️🏫 **Tuition Modes**

We provide:
- Online tuition
- Offline tuition
- Home tuition

Please share your area for proper guidance.

📞 {CONTACT_NUMBER}"""

    elif any(word in user_msg for word in ["timing", "time", "batch"]):
        return f"""⏰ **Class Timings**

Current batch timings: **{TIMINGS}**

For exact subject timing, please contact:
📞 **{CONTACT_NUMBER}**"""

    elif any(word in user_msg for word in ["contact", "phone", "mobile", "call", "number", "whatsapp"]):
        msg = "Assalamu Alaikum, I want admission details from Farooq Economics Academy."
        return f"""📞 **Contact Details**

Phone / WhatsApp: **{CONTACT_NUMBER}**  
Email: **{EMAIL}**  
Location: **{LOCATION}**

👉 {make_whatsapp_link(msg)}"""

    else:
        return f"""Thank you 😊

I can help you with:
- Admission
- Fees
- Demo class
- Subjects
- Online / Offline / Home tuition
- Parent guidance

📞 WhatsApp: **{CONTACT_NUMBER}**"""


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

    return f"""✅ **Your enquiry has been saved successfully.**

Now click below to send it on WhatsApp:

👉 {make_whatsapp_link(whatsapp_message)}
"""


custom_css = """
.gradio-container {
    background: linear-gradient(135deg, #000000 0%, #111111 45%, #c9a227 100%) !important;
    font-family: Arial, sans-serif;
}

/* Main white cards */
.main-card {
    background: #ffffff;
    color: #111111;
    border-radius: 18px;
    padding: 28px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.28);
    margin-bottom: 18px;
}

/* Hero section */
.hero {
    text-align: center;
    background: linear-gradient(135deg, #000000, #1a1a1a);
    color: #ffffff;
    padding: 35px;
    border-radius: 22px;
    border: 3px solid #c9a227;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

.hero h1 {
    font-size: 42px;
    margin-bottom: 10px;
    color: #c9a227;
}

.hero p {
    font-size: 18px;
    color: #ffffff;
}

.gold {
    color: #c9a227;
    font-weight: bold;
}

/* Grid layout */
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 15px;
}

/* White info cards */
.info-card {
    background: #ffffff;
    color: #111111;
    border-left: 6px solid #c9a227;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.12);
}

.info-card h3 {
    color: #111111;
    margin-top: 0;
}

/* Fee cards */
.fee-card {
    background: #111111;
    color: #ffffff;
    border-radius: 14px;
    padding: 18px;
    text-align: center;
    border: 2px solid #c9a227;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
}

.fee-card h3 {
    color: #c9a227;
}

/* CTA buttons */
.cta-button {
    display: inline-block;
    padding: 13px 24px;
    margin: 8px;
    border-radius: 30px;
    text-decoration: none;
    font-weight: bold;
    color: #000000;
    background: #c9a227;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

.cta-button:hover {
    background: #e0b93a;
}

/* Section titles */
.section-title {
    color: #111111;
    text-align: center;
    font-size: 28px;
    margin-top: 10px;
    margin-bottom: 16px;
}

/* Fix Gradio text visibility */
.gr-markdown, .gr-markdown p, .gr-markdown h1, .gr-markdown h2, .gr-markdown h3,
.gradio-container label, .gradio-container .prose, .gradio-container .prose * {
    color: #ffffff !important;
}

/* Input labels on dark background */
label {
    color: #ffffff !important;
    font-weight: 600;
}

/* Chatbox and form area */
.gr-chatbot, .gr-box, .gr-form, .gr-group {
    background: #ffffff !important;
    color: #111111 !important;
    border-radius: 14px !important;
}

/* Input text */
textarea, input, select {
    color: #111111 !important;
}
"""


with gr.Blocks(title="Farooq Economics Academy", css=custom_css) as demo:

    gr.HTML(f"""
    <div class="hero">
        <h1>🎓 {ACADEMY_NAME}</h1>
        <p>Empowering Intermediate Students for Academic Success</p>
        <p><span class="gold">Civics | Economics | Commerce | Accountancy</span></p>
        <p>Online • Offline • Home Tuition Available</p>
        <a class="cta-button" href="tel:{CONTACT_NUMBER}">📞 Call Now</a>
        <a class="cta-button" href="https://wa.me/{WHATSAPP_NUMBER}" target="_blank">💬 WhatsApp Now</a>
    </div>
    """)

    gr.HTML("""
    <div class="main-card">
        <h2 class="section-title">⭐ Why Choose Us?</h2>
        <div class="card-grid">
            <div class="info-card"><h3>📘 Concept Clarity</h3><p>Step-by-step explanation for better understanding.</p></div>
            <div class="info-card"><h3>👨‍🏫 Personal Attention</h3><p>Support for weak and average students.</p></div>
            <div class="info-card"><h3>📝 Exam Focused</h3><p>Preparation according to exam needs.</p></div>
            <div class="info-card"><h3>✅ Demo Class</h3><p>Demo class available for students.</p></div>
        </div>
    </div>
    """)

    gr.HTML("""
    <div class="main-card">
        <h2 class="section-title">💰 Fee Structure</h2>
        <div class="card-grid">
            <div class="fee-card"><h3>1st Year</h3><p>₹6,000</p></div>
            <div class="fee-card"><h3>2nd Year</h3><p>₹8,000</p></div>
            <div class="fee-card"><h3>Per Subject</h3><p>₹6,000</p></div>
            <div class="fee-card"><h3>All 3 Subjects</h3><p>₹10,000<br>Save ₹2,000</p></div>
        </div>
    </div>
    """)

    gr.Markdown("## 🤖 Smart Academy Counsellor")
    gr.ChatInterface(
        fn=chatbot,
        title="Farooq Economics Academy AI Assistant",
        description="Ask about admissions, fees, demo class, subjects, home tuition, and parent guidance."
    )

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

    gr.HTML(f"""
    <div class="main-card">
        <h2 class="section-title">📍 Academy Details</h2>
        <p><b>Academy:</b> {ACADEMY_NAME}</p>
        <p><b>Location:</b> {LOCATION}</p>
        <p><b>Timings:</b> {TIMINGS}</p>
        <p><b>Contact:</b> {CONTACT_NUMBER}</p>
        <p><b>Email:</b> {EMAIL}</p>
    </div>
    """)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
