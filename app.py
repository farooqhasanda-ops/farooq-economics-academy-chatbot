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

    whatsapp_message = f"""
Assalamu Alaikum Sir,

🎓 New Admission Inquiry

👤 Student Name: {name}
📱 Phone: {phone}
📚 Class: {student_class}
💻 Mode: {mode}

Please contact me regarding admission.
"""

    whatsapp_link = f"https://wa.me/919989221983?text={whatsapp_message.replace(' ', '%20').replace(chr(10), '%0A')}"

    return f"""
✅ Admission Inquiry Submitted Successfully!

💬 Click the button below to send your details on WhatsApp:

<a href="{whatsapp_link}" target="_blank">
<button style="background-color:#25D366;color:white;padding:12px 20px;border:none;border-radius:8px;font-size:18px;font-weight:bold;">
💬 Send Admission Details on WhatsApp
</button>
</a>
"""
