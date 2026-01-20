# 🏢 DomainScout: The B2B Startup Assistant

> **Built for Droidrun DevSprint 2026** | **Track:** B2B Automation

## 🚀 Overview
**DomainScout** is a mobile-native AI agent built on the **Droidrun Framework**. It automates one of the most repetitive tasks for new entrepreneurs: checking domain name availability.

Instead of manually opening a browser, typing a URL, searching, and reading results, DomainScout autonomously navigates the **GoDaddy mobile site** to verify availability and pricing in real-time.

## 🎥 Demo Video
### 
*(The video `demo_video.mp4` is located in the `src/` folder of this repository. Click the link above to view it.)*

## 💡 The Problem (B2B Use Case)
For branding agencies and startup founders, finding an available `.com` domain is a bottleneck.
* **Manual Friction:** Requires constant app switching.
* **Mobile Unfriendly:** Checking bulk domains on mobile is tedious.
* **Time Consuming:** Takes 3-5 minutes per domain manually.

## ✅ The Solution
DomainScout reduces this to **seconds**.
1.  **Input:** User asks "Is 'DroidRunPizza' available?"
2.  **Action:** Agent launches Chrome and navigates to GoDaddy.
3.  **Extraction:** Agent interprets the visual result (Available vs Taken).
4.  **Reporting:** Agent reports the price instantly.

## 🤖 Workflow & Architecture
The agent follows a strict **"Observe-Think-Act"** loop using Mobilerun Cloud:

1.  **Navigation:** Opens `Chrome` -> `godaddy.com`.
2.  **Input Action:** Types the target domain into the search bar.
3.  **Visual Analysis:** Identifying UI elements like "Exact Match" or "Taken".
4.  **Data Extraction:** Parsing the price (e.g., ₹499.00).

## 🛠️ Tech Stack
* **Framework:** [Droidrun](https://github.com/droidrun/droidrun) (Mobile Agent Framework)
* **Platform:** Mobilerun Cloud (Android Emulator)
* **Browser:** Google Chrome Mobile
* **LLM:** GPT-4o / Gemini Pro (via Droidrun)

## 📦 Installation & Usage

1.  **Clone the Repo**
    ```bash
    git clone [https://github.com/Nikitajhajharia/DomainScout-DroidRun.git]
    cd DomainScout-DroidRun
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Agent**
    Ensure your device/emulator is connected via ADB.
    ```bash
    python src/main.py
    ```

## 🔮 Future Roadmap (Round 2 Plans)
* **Bulk Search:** Check 10 domains in a row.
* **Purchase Automation:** Add the domain to the cart automatically.
* **Alternatives:** Suggest alternative names if the domain is taken.

## 📄 License
MIT License
