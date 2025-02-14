import streamlit as st
from streamlit.components.v1 import html

st.title("Streamlit App with Floating Chatbot")

# HTML, CSS, and JavaScript code
chatbot_html = """
<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="utf-8">
  <title>Chatbot in JavaScript | CodingNepal</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <!-- Google Fonts Link For Icons -->
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,400,1,0" />
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: "Poppins", sans-serif;
    }
    body {
      background: #E3F2FD;
      margin: 0;
      padding: 0;
    }
    .chatbot-toggler {
      position: fixed;
      top: 15px; /* Adjusted position for top right corner */
      right: 15px; /* Adjusted position for top right corner */
      outline: none;
      border: none;
      height: 50px;
      width: 50px;
      display: flex;
      cursor: pointer;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      background: #724ae8;
      transition: all 0.2s ease;
      z-index: 1000;
    }
    body.show-chatbot .chatbot-toggler {
      transform: rotate(90deg);
    }
    .chatbot-toggler span {
      color: #fff;
      position: absolute;
    }
    .chatbot-toggler span:last-child,
    body.show-chatbot .chatbot-toggler span:first-child  {
      opacity: 0;
    }
    body.show-chatbot .chatbot-toggler span:last-child {
      opacity: 1;
    }
    .chatbot {
      position: fixed;
      top: 70px; /* Positioning it below the toggler icon */
      right: 15px; /* Align with the toggler icon */
      width: 420px;
      background: #fff;
      border-radius: 15px;
      overflow: hidden;
      opacity: 0;
      pointer-events: none;
      transform: scale(0.5);
      transform-origin: top right; /* Scale from the top right */
      box-shadow: 0 0 128px 0 rgba(0,0,0,0.1),
                  0 32px 64px -48px rgba(0,0,0,0.5);
      transition: all 0.1s ease;
      z-index: 1000;
    }
    body.show-chatbot .chatbot {
      opacity: 1;
      pointer-events: auto;
      transform: scale(1);
    }
    .chatbot header {
      padding: 16px 0;
      position: relative;
      text-align: center;
      color: #fff;
      background: #724ae8;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .chatbot header span {
      position: absolute;
      right: 15px;
      top: 50%;
      display: none;
      cursor: pointer;
      transform: translateY(-50%);
    }
    header h2 {
      font-size: 1.4rem;
    }
    .chatbot .chatbox {
      overflow-y: auto;
      height: 510px;
      padding: 30px 20px 100px;
    }
    .chatbot :where(.chatbox, textarea)::-webkit-scrollbar {
      width: 6px;
    }
    .chatbot :where(.chatbox, textarea)::-webkit-scrollbar-track {
      background: #fff;
      border-radius: 25px;
    }
    .chatbot :where(.chatbox, textarea)::-webkit-scrollbar-thumb {
      background: #ccc;
      border-radius: 25px;
    }
    .chatbox .chat {
      display: flex;
      list-style: none;
    }
    .chatbox .outgoing {
      margin: 20px 0;
      justify-content: flex-end;
    }
    .chatbox .incoming span {
      width: 32px;
      height: 32px;
      color: #fff;
      cursor: default;
      text-align: center;
      line-height: 32px;
      align-self: flex-end;
      background: #724ae8;
      border-radius: 4px;
      margin: 0 10px 7px 0;
    }
    .chatbox .chat p {
      white-space: pre-wrap;
      padding: 12px 16px;
      border-radius: 10px 10px 0 10px;
      max-width: 75%;
      color: #fff;
      font-size: 0.95rem;
      background: #724ae8;
    }
    .chatbox .incoming p {
      border-radius: 10px 10px 10px 0;
    }
    .chatbox .chat p.error {
      color: #721c24;
      background: #f8d7da;
    }
    .chatbox .incoming p {
      color: #000;
      background: #f2f2f2;
    }
    .chatbot .chat-input {
      display: flex;
      gap: 5px;
      position: absolute;
      bottom: 0;
      width: 100%;
      background: #fff;
      padding: 3px 20px;
      border-top: 1px solid #ddd;
    }
    .chat-input textarea {
      height: 55px;
      width: 100%;
      border: none;
      outline: none;
      resize: none;
      max-height: 180px;
      padding: 15px 15px 15px 0;
      font-size: 0.95rem;
    }
    .chat-input span {
      align-self: flex-end;
      color: #724ae8;
      cursor: pointer;
      height: 55px;
      display: flex;
      align-items: center;
      visibility: hidden;
      font-size: 1.35rem;
    }
    .chat-input textarea:valid ~ span {
      visibility: visible;
    }

    @media (max-width: 490px) {
      .chatbot-toggler {
        right: 15px;
        top: 15px; /* Adjust position for smaller screens */
      }
      .chatbot {
        right: 15px;
        top: 70px; /* Position below the toggler for smaller screens */
        height: 100%;
        border-radius: 0;
        width: 100%;
      }
      .chatbot .chatbox {
        height: 90%;
        padding: 25px 15px 100px;
      }
      .chatbot .chat-input {
        padding: 5px 15px;
      }
      .chatbot header span {
        display: block;
      }
    }
  </style>
</head>
<body>
  <button class="chatbot-toggler">
    <span class="material-symbols-rounded">mode_comment</span>
    <span class="material-symbols-outlined">close</span>
  </button>
  <div class="chatbot">
    <header>
      <h2>Chatbot</h2>
      <span class="close-btn material-symbols-outlined">close</span>
    </header>
    <ul class="chatbox">
      <li class="chat incoming">
        <span class="material-symbols-outlined">smart_toy</span>
        <p>Hi there 👋<br>How can I help you today?</p>
      </li>
    </ul>
    <div class="chat-input">
      <textarea placeholder="Enter a message..." spellcheck="false" required></textarea>
      <span id="send-btn" class="material-symbols-rounded">send</span>
    </div>
  </div>
  <script>
    const chatbotToggler = document.querySelector(".chatbot-toggler");
    const closeBtn = document.querySelector(".close-btn");
    const chatbox = document.querySelector(".chatbox");
    const chatInput = document.querySelector(".chat-input textarea");
    const sendChatBtn = document.querySelector(".chat-input span");

    let userMessage = null; // Variable to store user's message
    const API_KEY = "PASTE-YOUR-API-KEY"; // Paste your API key here
    const inputInitHeight = chatInput.scrollHeight;

    const createChatLi = (message, className) => {
      // Create a chat <li> element with passed message and className
      const chatLi = document.createElement("li");
      chatLi.classList.add("chat", `${className}`);
      let chatContent = className === "outgoing" ? `<p></p>` : `<span class="material-symbols-outlined">smart_toy</span><p></p>`;
      chatLi.innerHTML = chatContent;
      chatLi.querySelector("p").textContent = message;
      return chatLi; // return chat <li> element
    }

    const generateResponse = (chatElement) => {
      const API_URL = "https://api.openai.com/v1/chat/completions";
      const messageElement = chatElement.querySelector("p");

      // Define the properties and message for the API request
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
          model: "gpt-3.5-turbo",
          messages: [{role: "user", content: userMessage}],
        })
      }

      // Send POST request to API, get response and set the response as paragraph text
      fetch(API_URL, requestOptions).then(res => res.json()).then(data => {
        messageElement.textContent = data.choices[0].message.content.trim();
      }).catch(() => {
        messageElement.classList.add("error");
        messageElement.textContent = "Oops! Something went wrong. Please try again.";
      }).finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
    }

    const handleChat = () => {
      userMessage = chatInput.value.trim(); // Get user entered message and remove extra whitespace
      if (!userMessage) return;

      // Clear the input textarea and set its height to default
      chatInput.value = "";
      chatInput.style.height = `${inputInitHeight}px`;

      // Append the user's message to the chatbox
      chatbox.appendChild(createChatLi(userMessage, "outgoing"));
      chatbox.scrollTo(0, chatbox.scrollHeight);

      setTimeout(() => {
        // Display "Thinking..." message while waiting for the response
        const incomingChatLi = createChatLi("Thinking...", "incoming");
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
      }, 600);
    }

    chatInput.addEventListener("input", () => {
      // Adjust the height of the input textarea based on its content
      chatInput.style.height = `${inputInitHeight}px`;
      chatInput.style.height = `${chatInput.scrollHeight}px`;
    });

    chatInput.addEventListener("keydown", (e) => {
      // If Enter key is pressed without Shift key and the window 
      // width is greater than 800px, handle the chat
      if (e.key === "Enter" && !e.shiftKey && window.innerWidth > 800) {
        e.preventDefault();
        handleChat();
      }
    });

    sendChatBtn.addEventListener("click", handleChat);
    closeBtn.addEventListener("click", () => document.body.classList.remove("show-chatbot"));
    chatbotToggler.addEventListener("click", () => document.body.classList.toggle("show-chatbot"));
  </script>
</body>
</html>

"""

# Display the chatbot interface in the Streamlit app
html(chatbot_html, height=800)
