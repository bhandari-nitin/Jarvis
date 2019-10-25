# Jarvis - The ChatBot

## Introduction 
> This is a conversational bot using IBM Watson API for getting doctor-recommendations based on location integrated with slack and uses [**BetterDoctor API**](https://developer.betterdoctor.com/documentation15).

### Documentaion
- [Ideation and Scoping](#ideation-and-scoping)
- [Content ](#content)
- [Intents](#intents)
- [API Integration](#api-integration)
- [Use of Advanced NLP Features](#use-of-advanced-nlp-features)
- [Quality Assurance](#quality-assurance)

### Ideation and Scoping
  - [x] Documentation of ideation, content, and functionality
  - [ ] Documentaion of Scope in format of User Stories/other format of your choice
  
  Turning a chatbot idea requires a complete step-by-step chatbot strategy from goal defination to publishing and maintainence. 
  
   1. **Defining Goals**\
        Jarvis will connect to BetterDoctor API to recommend doctors based on the location. Creating a chatbot there are many things to define before starting

   2. **Understand Users**\
        We generally try to understand the user-base to keep the conversational dialog consistent and use/not use different slangs as well. 

   3. **Tools**\
        Jarvis uses [Better Doctor API](https://developer.betterdoctor.com/documentation15) to recommend doctors bases on location, and is based on IBM's Watson Assistant and IBM's Cloud Functions to write the Python script to fetch the results from the BetterDoctor API.

   4. **Product Requirements/Scope**\
        One of the important steps in this strategy is documenting product requirements and is focused precisely on shaping a chatbot idea into a working project. I am using **User Stories Framework** to document requirements.The idea behind **high-level user-stories**  is to be in your customer's shoes and that will give a prespective of their expectations from the product, in this case Jarvis. 
        
        **As a** Customer **(who)**
        - **I need** Jarvis to recommend me doctors based on location I provide  **(what) so that** I can be at airport on time **(why)**
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**

   5. **Prioritize expectations from the chatbot**\
        Since this is a functional demo and we are just asking Jarvis one special task, from a customer point of view, I would expect Jarvis to provide the status of the flight whenever asked. 

   6. **Design a Conversational Flow**\
        Chatbots needs to plan their dialog use cases in advance to engage with the user and do not get lost in the conversation. The most important feature is to create a **personality** of the chatbot that is consistent throughout the engagement. Conversational flow is a dialog tree sure every user request is covered by some part of the bot’s logics. 
        
         1. **User Onboarding**  
         - Chatbot should give an introduction along with quick overview of it's abilities
          
         2. **Intents**
         - We want Jarvis to handle user-intents related:
         - #Greetings/Introduction
         - #Get Doctor's Information
         - #Escalate
         - #Disambiguate
         - #Good Bye
         - #Thank You
         
         3. **Confirm Understanding**
         - Keeping user informed at each step of the conversation is crucial to prevent any ambiguity. 
         
         4. **Design the dialog in a optimized way**
         - Responses/questions should be precise and straightforward sentences/questions
         - Avoiding open-ended questions
         - Following the natural flow of a conversation
         - Diversify bot's replies whenever possible 
         
         5. **Be consistent with Bot's persona**
         - Use the communication style to stay consistent with the chatbot's personality
         
         6. **Provide visual clues**
         - It's a good idea to add visual cards when explaining the difference between several things or products
       
   7. **Monitor the analytics once deployed to the customers**\
        This is a future step to incorporate, analyzing failure issues and patterns backtracking to imporvising intents, utterances, etc. 
  

### Content
  - [ ] Creativity of creating the dialog to develop orignal conversational content
  - _Note: The output is the spoken and not displayed as text on screen. People generally speak differently than how they write_
 
### Intents
  - [x] Optimize the sample intents to capture the most common ways someone may say a certian intent, while using **no more than 10 unique intents**

### API Integration
  - [ ] Syntax, following the Object Oriented Principles, and general convention / best practices of the selected microservice language. 
  - [ ] Proper Implementation of RESTful or SOAP API, taking into account a reasonable range of scenarios and parameters. 
  - [ ] Implement error handling that produces a user friendly message
  - [ ] Transform JSON/XML data to a string that can be spoken in the target human language

### Use of Advanced NLP Features
  - [ ] Proper implementation of at least two of the following advanced NLP features:
       - [ ] Digressions
       - [ ] Pattern Entities
       - [ ] Slots / Variables
       - [ ] Dual simultaneous Intents / Follow-Up Intents

### Quality Assurance
  - [ ] Overall quality of the final corpus and user experience
  - _Note: Generally the measurement for this would be how many unexpected errors or behaviours were encountered_ 

---

## Tools/Tech 
* IBM Watson API
* Python3

---

## Installing

To install python3, use brew for macs:
``` 
brew install python3
```

---

## Interacting with Jarvis

Go to your favourite browser and hit the below URL to receive invitaion to join the slack workspace.
```
https://join.slack.com/t/jarvisincgroup/shared_invite/enQtNzkyMjk4OTY0NDgzLWM0Y2VmNTIzODdmOWNmMjUyZTVkN2U3NzZiYTc0N2EyMDBmZWFjOTU4ZmE3MTA4NjMzOWFmNTIyMDJhNjRhMzA
```

---

## Authors
* **Nitin Bhandari** 

---

## Acknowledgements

1. [Define chatbot strategy](https://www.digiteum.com/10-steps-to-define-your-chatbot-strategy/)
2. [Document chatbot requirements](https://chatbotsmagazine.com/how-to-document-chatbot-requirements-7df81275cc66)
3. [Conversation Design](https://www.digiteum.com/conversational-ux-7-tips-creating-effective-chatbot-user-experience/)
