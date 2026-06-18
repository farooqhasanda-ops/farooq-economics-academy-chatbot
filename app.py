import gradio as gr

academy_info = {
    "academy_name": "Farooq Economics Academy",
    "founder": "Farooq Hasan",
    "experience": "20+ Years Teaching Experience",
    "subjects": "Economics, Civics, Commerce, Accounts",
    "classes": "Intermediate 1st Year and 2nd Year",
    "timings": "Please contact the academy",
    "contact": "+91 9989221983",
    "email": "frkfarooqhasan@gmail.com",
    "location": "Tolichowki, Hyderabad",
    "fees": "Please contact the academy for latest fee details"
}

def chatbot(message, history):
    msg = message.lower().strip()

    if any(word in msg for word in ["subject", "subjects", "course", "courses"]):
        return f"📚 Subjects Offered:\n\n{academy_info['subjects']}"

    if any(word in msg for word in ["contact", "phone", "mobile", "call"]):
        return f"📞 Contact Number:\n{academy_info['contact']}\n\n📧 Email:\n{academy_info['email']}"

    if any(word in msg for word in ["location", "address", "where"]):
        return f"📍 Location:\n{academy_info['location']}"

    if any(word in msg for word in ["experience", "years"]):
        return f"👨‍🏫 {academy_info['experience']}"

    if any(word in msg for word in ["fee", "fees", "cost", "price"]):
        return """
💰 Fee Information

Please share:

• Student Name
• Class
• Mobile Number

Our academy team will guide you with the latest fee structure.
"""

    if any(word in msg for word in ["class", "classes", "intermediate", "1st year", "2nd year"]):
        return f"🎓 Classes Available:\n\n{academy_info['classes']}"

    if any(word in msg for word in ["admission", "join", "enroll", "admissions"]):
        return f"""
🎓 Admission Inquiry

Please share:

1. Student Name
2. Mobile Number
3. Class (1st Year / 2nd Year)
4. Online or Offline

📞 Contact: {academy_info['contact']}
"""

    if "whatsapp" in msg:
        return f"""
📱 WhatsApp Support

Please contact:

{academy_info['contact']}
"""

    return """
Assalamu Alaikum! 👋

Welcome to Farooq Economics Academy.

I can help you with:

✅ Admissions
✅ Economics Tuition
✅ Fee Information
✅ Online Classes
✅ Offline Classes
✅ WhatsApp Support

How may I help you today?
"""

demo = gr.ChatInterface(chatbot)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
