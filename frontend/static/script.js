// script.js

const chatInput = 
    document.querySelector('.chat-input textarea');
const sendChatBtn = 
    document.querySelector('.chat-input button');
const chatbox = document.querySelector(".chatbox");
let userMessage;
const API_KEY = "KEYNOTNEEDEDANDTOBEIMPLEMENTEDINFUTURE"; 
const API_BASE_URL="http://ec2-13-220-163-222.compute-1.amazonaws.com:8081"

const createChatLi = (message, className) => {
    const chatLi = document.createElement("li");
    chatLi.classList.add("chat", className);
    let chatContent = 
        className === "chat-outgoing" ? `<p>${message}</p>` : `<p>${message}</p>`;
    chatLi.innerHTML = chatContent;
    return chatLi;
}

const generateResponse = (incomingChatLi) => {
    const API_URL = API_BASE_URL+"/invoke";
    const messageElement = incomingChatLi
    .querySelector("p");
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            "model": "bedrockAgents",
            "messages": [
                {
                    role: "user",
                    content: userMessage
                }
            ]
        })
    };

    fetch(API_URL, requestOptions)
        .then(res => {
            if (!res.ok) {
                throw new Error("Network response was not ok");
            }
            return res.json();
        })
        .then(json => {
            console.log(json)
            messageElement
            .textContent = json["data"]["message"]["content"];
            chatInput.placeholder="Is there anything else that I can help you with?..."; 
            
        })
        .catch((error) => {
            console.log('>>> in CATCH block, error is =>', error);
            console.log('>>> in CATCH block, error name is =>', error.name);
            console.log('>>> in CATCH block, error message is =>', error.message);
            messageElement
            .classList.add("error");
            messageElement
            .textContent = "I am unable to handle this request. Please call 1-800-AWS-AGENT for assistance.";
        })
        .finally(() => chatbox.scrollTo(0, chatbox.scrollHeight));
};


const handleChat = () => {
    userMessage = chatInput.value.trim();
    if (!userMessage) {
        return;
    }
    chatbox
    .appendChild(createChatLi(userMessage, "chat-outgoing"));
    chatbox
    .scrollTo(0, chatbox.scrollHeight);
    setTimeout(() => {
        const incomingChatLi = createChatLi("Thinking...", "chat-incoming")
        chatbox.appendChild(incomingChatLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);
        generateResponse(incomingChatLi);
    }, 1200);
}

sendChatBtn.addEventListener("click", handleChat);

function cancel() {
    let chatbotcomplete = document.querySelector(".chatBot");
    if (chatbotcomplete.style.display != 'none') {
        chatbotcomplete.style.display = "none";
        let lastMsg = document.createElement("p");
        lastMsg.textContent = 'Thanks for using our customer support agent!';
        lastMsg.classList.add('lastMessage');
        document.body.appendChild(lastMsg)
    }
}

const initialize = () => {
    sendChatBtn.disabled=true;
    chatInput.placeholder="Initializing the chat agent,please wait ...";
    const API_URL = API_BASE_URL+"/initialize";
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({
            "model": "bedrockAgents",
            "messages": [
                {
                    role: "user",
                    content: userMessage
                }
            ]
        })
    };

    fetch(API_URL, requestOptions)
        .then(res => {
            if (!res.ok) {
                throw new Error("Network response was not ok");
            }
            return res.json();
        })
        .then(json => {
            console.log(json)
        })
        .catch((error) => {
            console.log('>>> in CATCH block, error is =>', error);
            console.log('>>> in CATCH block, error name is =>', error.name);
            console.log('>>> in CATCH block, error message is =>', error.message);
            messageElement
            .classList.add("error");
            messageElement
            .textContent = "Oops! Something went wrong. Please try again!";
        })
        .finally(() => {
            chatbox.scrollTo(0, chatbox.scrollHeight);
            chatInput.placeholder="Agents Ready, How can I help you? ..."
            sendChatBtn.disabled=false;

        });
}
window.onload=initialize