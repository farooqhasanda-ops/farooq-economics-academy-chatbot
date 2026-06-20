import gradio as gr

academy_info = {
    "academy_name": "Farooq Economics Academy",
    "founder": "Farooq Hasan",
    "experience": "20+ Years Teaching Experience",
    "subjects": "Economics, Civics, Commerce, Accounts",
    "classes": "1st Year CEC and 2nd Year CEC",
    "contact": "+91 9989221983",
    "email": "frkfarooqhasan@gmail.com",
    "location": "Tolichowki, Hyderabad",
    "whatsapp": "https://wa.me/919989221983",
    "admission_form": "https://docs.google.com/forms/d/e/1FAIpQLSeeXFxUPek9vKkjoVLLoGqNvbWPhm6EISnCN9vpGFpTcPtrow/viewform?usp=publish-editor",
    "maps": "https://www.google.com/maps/search/?api=1&query=Tolichowki+Hyderabad"
}

def chatbot(message, history):
    msg = message.lower().strip()

    if any(word in msg for word in ["fee", "fees", "cost", "price"]):
        return "💰 Please fill the Admission Form or contact us on WhatsApp for latest fee details."

    if any(word in msg for word in ["admission", "join", "enroll", "register"]):
        return f"🎓 Please fill the Admission Form here:\n{academy_info['admission_form']}"

    if any(word in msg for word in ["contact", "phone", "call", "mobile"]):
        return f"📞 Phone: {academy_info['contact']}\n📧 Email: {academy_info['email']}"

    if "whatsapp" in msg:
        return f"💬 WhatsApp Support:\n{academy_info['whatsapp']}"

    if any(word in msg for word in ["location", "address", "where", "map", "maps"]):
        return f"📍 Location: {academy_info['location']}\n🗺️ Google Maps: {academy_info['maps']}"

    if any(word in msg for word in ["subject", "subjects", "course", "courses"]):
        return f"📚 Subjects Offered:\n{academy_info['subjects']}"

    return """
Assalamu Alaikum! 👋

Welcome to Farooq Economics Academy.

✅ 1st Year CEC
✅ 2nd Year CEC
✅ Economics Tuition
✅ Online & Offline Classes
✅ Admission Enquiry
✅ WhatsApp Support

How may I help you today?
"""

with gr.Blocks(title="Farooq Economics Academy") as demo:

    try:
        gr.Image("logo.png", width=220, show_label=False)
    except:
        pass

    gr.Markdown(f"""
# 🎓 Farooq Economics Academy

### Learn • Understand • Succeed

<a href="tel:+919989221983" target="_blank">
<button style="background-color:#28a745;color:white;padding:12px 20px;border:none;border-radius:8px;font-size:18px;margin:5px;">
📞 Call Now
</button>
</a>

<a href="https://wa.me/919989221983" target="_blank">
<button style="background-color:#25D366;color:white;padding:12px 20px;border:none;border-radius:8px;font-size:18px;margin:5px;">
💬 WhatsApp Now
</button>
</a>

<a href="{academy_info['admission_form']}" target="_blank">
<button style="background-color:#6f42c1;color:white;padding:12px 20px;border:none;border-radius:8px;font-size:18px;margin:5px;">
📝 Admission Form
</button>
</a>

<a href="{academy_info['maps']}" target="_blank">
<button style="background-color:#007bff;color:white;padding:12px 20px;border:none;border-radius:8px;font-size:18px;margin:5px;">
📍 Google Maps
</button>
</a>

---

### 📍 Location
Tolichowki, Hyderabad

### 📞 Contact
+91 9989221983

---
""")

    gr.ChatInterface(chatbot)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
