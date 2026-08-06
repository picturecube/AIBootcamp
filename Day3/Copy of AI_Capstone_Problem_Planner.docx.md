**AI CAPSTONE PROJECT PLANNER**

*Azielon AI Bootcamp  —  Day 10 Capstone / AI Innovation Expo*

Name(s): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_     Team/Track: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

*Fill this out before you write any code, in order. Don't skip ahead — each step only works if the one before it is answered specifically, not broadly.*

# **Step 1: Start With the Big Idea**

**What's the general problem you care about? (It's OK if this is broad right now.)**

| Some people do not have access to computers, and they will have a hard time surviving in the modern world where everyone assumes them to be fluent with technology. |
| :---- |

# **Step 2: Narrow It Down (the funnel)**

Answer these in order. Each answer should be smaller and more specific than the last.

## **2a. Pick ONE specific subject**

(Not a whole category — just one.)

**Your subject:**

| Computer problem |
| :---- |

***Gut check:** Could I find or collect 20+ real examples of just this one thing?*

## **2b. Pick ONE way the user gives you information**

(One type of input, given the same way every time.)

**Your input type:**

| Text |
| :---- |

***Gut check:** Am I always looking at the same kind of input, in the same format, every time?*

## **2c. Pick 2–4 SPECIFIC categories/outcomes to tell apart**

(Name them exactly — not “what's wrong” or “what it is.”)

**1\.**

| Basic computer usage |
| :---- |

**2\.**

| Simple computer problems |
| :---- |

**3\.**

| Navigating useful apps |
| :---- |

**4\.**

| Changing settings |
| :---- |

***Gut check:** Can I find or collect 10–15 real examples for EACH one? If not, cut it from the list.*

## **2d. Pick ONE clear result/action for each category**

(One short output each, not a paragraph.)

**Your results/actions:**

| A lesson or solution |
| :---- |

## **2e. Say what your app will NOT do**

(This protects you from scope creep.)

**Out of scope:**

| Will not do tasks on the computer by itself or help with anything that isn’t related to computers |
| :---- |

# **Step 3: The One-Sentence Test**

Read this out loud, filled in with your Step 2 answers:

*“My app looks at a \[input from 2b\] of/about \[subject from 2a\], tells the user which of \[categories from 2c\] it is, and gives them \[result from 2d\].”*

***Gut check:** Could I say this in one breath? If not, cut a category and try again.*

**Your final Problem Statement: “Many first-time computer users struggle with surviving in the world because the world assumes they know how to use computers.”**

| Many first-time computer users struggle with surviving in the world because the world assumes they know how to use computers. |
| :---- |

# **Step 4: Name Your AI App**

**App Name:**

| The Device Teacher |
| :---- |

**One-line pitch: “\[App Name\] helps \[who\] do \[what\] by \[how\].”**

| The Device Teacher helps first-time computer users learn to use a computer by teaching computer concepts by adapting to the user’s learning style. |
| :---- |

# **Step 5: INPUT — What goes INTO your app?**

| Question | Your Answer |
| :---- | :---- |
| What does the user upload/type/click? | What they need help with or what they want to learn |
| What format? (photo, text, number, file) | text |
| ONE real example of actual input | Help with how to access the internet |

# **Step 6: PROCESS — What does the AI/app DO with it?**

| Question | Your Answer |
| :---- | :---- |
| Steps in order (1, 2, 3…) | Takes the user input and adds it to a descriptive prompt that goes into an AI LLM The topic is researched by a new AI The AI gives instructions to the user |
| Which part is AI/ML vs. regular code/logic? | The code is handling the prompt, and the AI is processing the prompt and giving instructions to the user. |
| What tool/model/library handles the AI part? | OpenAI and Keras |
| What could go wrong, and how do you handle it? | If the user types in something that doesn’t make sense, the LLM will figure it out and clarify to the user the correct way to phrase their problem. |

# **Step 7: OUTPUT — What comes OUT for the user?**

| Question | Your Answer |
| :---- | :---- |
| What does the user see/get? | Step-by-step simple instructions |
| ONE real example of output, matching your Step 5 example | Step 1\. Move the mouse so the mouse is over the icon that looks like ![][image1] Step 2\. Press the left mouse button Step 3\. Type anything using the keyboard to find it on the web and press the Enter key Step 4\. Click on the blue text to go to the webpage you want from the list |
| How does the user know it's correct/helpful? | The user will achieve their desired result of knowing how to access the Internet. |

# **Step 8: How Will You Know It Worked?**

**Success looks like:**

| The user gives feedback that says they were happy with the AI response. |
| :---- |

**One thing you'll test it on, live, on Day 10:**

| My computer |
| :---- |

# **Full Flow**

(Draw it or write it — fill each box with your Step 5–7 examples.)

| INPUT | PROCESS | OUTPUT |
| :---: | ----- | :---: |
| User enters “how do I access the internet” | Prompt: You are a mentor and I am a teacher of basic computer skills. A student asked me “how do I access the internet” and you need to tell me what topic to research. I only want a few words that I can use.  Output: use browser Prompt 2: You are a teacher of basic computer skills, and I am a student. How do I use browser? Explain to me simply. Output 2:  Step 1\. Move the mouse so the mouse is over the icon that looks like ![][image1] Step 2\. Press the left mouse button Step 3\. Type anything using the keyboard to find it on the web and press the Enter key Step 4\. Click on the blue text to go to the webpage you want from the list Prompt 3: You are a writer. Some people don’t understand this. Break down the steps and make them simpler for them, and display them. Do not lose any information in the process. Output 3: (Output 2 but broken down into more steps) Repeat based on user skill score | Output 3 Feedback form to help improve the program and tune the skill score |

# **Quick Gut-Check Questions**

Use these anytime you feel stuck or overwhelmed.

* Can I collect real examples for every category I listed? (If no → cut that category)

* Could I explain my whole project in one breath? (If no → it's still too big)

* If I had to demo this LIVE on Day 10 with an example I've never seen before, would it work? (If unsure → narrow further)

* Am I the one deciding what “counts” as each category, and could someone else look at it and agree with me? (If it's fuzzy to you, it'll be fuzzy to your AI)

*Keep this page — you'll present directly from it on Day 10\.*

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAUCAIAAADtKeFkAAAB6klEQVR4XmP4TxlgQBcgEeDUr3vwvt6hOzqHr+gcPax7ZCO6NAxg12964KXRoSd6hx7oHb6pffic7tGd1mcXoCsCAyz67fd+Nzn4zvjgS+PDT/UO3dM5fM3w+B7HC7O9b7aiK8Wq3+TAR4h+sBNA+o1P7Xa9PD3kXv3/X+iK0fUbH3jNmr6Mv3aPcOMBkbod6geB7r9odnKb29WpoQ+qk17koqlH1y804RBv7XG+npuCE++I9F4Sazmoc+SkyYl1zpf7Qu5XJT4rRFOPrp+t6ihX+22+7tsCfbcZ1AOAIryVu4yOLXK82B1wpzr8YRGaenT97PXXONtu8XTe5e26BRfUPzrV9lyz17VSv1uE3M9ed4Oz8QbICK92uKDJ0Qbzk2XOF7I8riYhqQUBdP2sNdcgRvD4T4aIaB6pMD2WbXo8ye5s9JdvX1GVY+hnqb4KMqL+Gk/QdN7Q+RBBnXMhhkfD//9AUQkB6PoZyi8CjWCrvc4TNAuo/+TjL2gK0AC6/m/fvjFXXQM6gSdwGlA/f/Ac0cB+iBSXeweqWhBA1w8EjBVXmKuucHv1QvTzB80Q8J8i6DdR1BsRonCARf9/sBFAX3D5T4HrF/CdgK4IDLDrBwKe3HNAI3h9+oGauezK0aVhAKd+IgGl+gE+jCCk/nDUigAAAABJRU5ErkJggg==>