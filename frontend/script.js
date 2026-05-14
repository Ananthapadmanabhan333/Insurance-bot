function sendMsg() {
    let box = document.getElementById("chat-box");
    let input = document.getElementById("msg");
    let text = input.value.trim();

    if (text === "") return;

    // User bubble
    let userMsg = document.createElement("div");
    userMsg.classList.add("user");
    userMsg.innerText = text;
    box.appendChild(userMsg);

    input.value = "";
    box.scrollTop = box.scrollHeight;

    showTyping();

    // Fake bot reply (replace later with backend)
    setTimeout(() => {
        hideTyping();

        let botMsg = document.createElement("div");
        botMsg.classList.add("bot");
        botMsg.innerText = getReply(text);
        box.appendChild(botMsg);

        box.scrollTop = box.scrollHeight;
    }, 1000);
}

function showTyping() {
    document.getElementById("typing").classList.remove("hidden");
}

function hideTyping() {
    document.getElementById("typing").classList.add("hidden");
}

// Fake simple replies
function getReply(q) {
    q = q.toLowerCase();

    if (q.includes("policy")) return "We offer health, motor, and travel insurance policies.";
    if (q.includes("claim")) return "To file a claim, provide your policy number and documents.";
    if (q.includes("renew")) return "You can renew your policy online within 30 days of expiry.";

    return "I'm here to help! Ask me anything about insurance.";
}
