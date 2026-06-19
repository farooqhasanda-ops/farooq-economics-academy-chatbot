import gradio as gr

academy_info = {
    "academy_name": "Farooq Economics Academy",
    "founder": "Farooq Hasan",
    "experience": "20+ Years Teaching Experience",
    "subjects": "Economics, Civics, Commerce, Accounts",
    "classes": "Intermediate 1st Year and 2nd Year",
    "contact": "+91 9989221983",
    "email": "frkfarooqhasan@gmail.com",
    "location": "Tolichowki, Hyderabad",
    "whatsapp": "https://wa.me/919989221983",
    "call": "tel:+919989221983"
}

def chatbot(message, history):
    msg = message.lower().strip()

    if any(word in msg for word in ["fee", "fees", "cost", "price"]):
        return "💰 Please share Student Name, Class and Mobile Number. Our team will guide you with fee details."

    if any(word in msg for word in ["admission", "join", "enroll", "register"]):
        return "🎓 Please share Name, Mobile Number, Class, and Online/Offline preference."

    if any(word in msg for word in ["contact", "phone", "call", "mobile"]):
        return f"📞 Call Now: {academy_info['contact']}\n\n💬 WhatsApp: {academy_info['whatsapp']}"

    if "whatsapp" in msg:
        return f"💬 WhatsApp Link:\n{academy_info['whatsapp']}"

    if any(word in msg for word in ["location", "address", "where"]):
        return f"📍 Location: {academy_info['location']}"

    if any(word in msg for word in ["subject", "subjects", "course", "courses"]):
        return f"📚 Subjects Offered: {academy_info['subjects']}"

    return """
Assalamu Alaikum! 👋

Welcome to Farooq Economics Academy.

I can help you with:
✅ Admissions
✅ Fee Information
✅ Online Classes
✅ Offline Classes
✅ WhatsApp Support

How may I help you today?
"""

def submit_form(name, phone, student_class, mode):
    if not name or not phone or not student_class or not mode:
        return "⚠️ Please fill all details."

    return f"""
✅ Admission Inquiry Submitted Successfully!

Student Name: {name}
Phone Number: {phone}
Class: {student_class}
Mode: {mode}

📞 Call: {academy_info['contact']}
💬 WhatsApp: {academy_info['whatsapp']}
"""

with gr.Blocks(title="Farooq Economics Academy") as demo:

    try:
        gr.Image("logo.png", width=220, show_label=False)
    except:
        pass

    gr.Markdown(f"""
# 🎓 Farooq Economics Academy

### Learn • Understand • Succeed

<a href="{academy_info['call']}" target="_blank">
<button style="background-color:#28a745;color:white;padding:12px 22px;border:none;border-radius:8px;font-size:18px;font-weight:bold;cursor:pointer;">
📞 Call Now
</button>
</a>

<a href="{academy_info['whatsapp']}" target="_blank">
<button style="background-color:#25D366;color:white;padding:12px 22px;border:none;border-radius:8px;font-size:18px;font-weight:bold;cursor:pointer;">
💬 WhatsApp Now
</button>
</a>

---
""")

    gr.ChatInterface(chatbot)

    gr.Markdown("## 📝 Admission Form")

    name = gr.Textbox(label="Student Name")
    phone = gr.Textbox(label="Phone Number")

    student_class = gr.Dropdown(
        ["Intermediate 1st Year", "Intermediate 2nd Year"],
        label="Class"
    )

    mode = gr.Radio(
        ["Online", "Offline"],
        label="Mode"
    )

    submit_btn = gr.Button("Submit Admission Inquiry")
    output = gr.Textbox(label="Status")

    submit_btn.click(
        submit_form,
        inputs=[name, phone, student_class, mode],
        outputs=output
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
