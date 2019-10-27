# Jarvis - The ChatBot

## Introduction 
> Jarvis is a functional-demo conversational bot using IBM Watson Assitant for getting doctor-recommendations based on location integrated with slack and uses [**BetterDoctor API**](https://developer.betterdoctor.com/documentation15) as third-party API.

### Documentaion
   - [Ideation and Scoping](#ideation-and-scoping)
   - [Content ](#content)
   - [Intents](#intents)
   - [API Integration](#api-integration)
   - [Use of Advanced NLP Features](#use-of-advanced-nlp-features)
   - [Quality Assurance](#quality-assurance)

### Ideation and Scoping
   - [x] Documentation of ideation, content, and functionality
   - [x] Documentaion of Scope in format of User Stories/other format of your choice
  
  Turning a chatbot idea requires a complete step-by-step chatbot strategy from goal defination to publishing and maintainence. 
  
   1. **Defining Goals**
         * For this functional demo, Jarvis will connect to BetterDoctor API to recommend doctors based on the location provided. 

   2. **Target Users**
         * We generally try to understand the user-base to keep the conversational dialog consistent and use/not use different slangs as well. 

   3. **Tools**
        * Jarvis is IMB Watson Assitant based conversational-bot that uses [Better Doctor API](https://developer.betterdoctor.com/documentation15) hosted on IBM Cloud Function to recommend doctors bases on location provided by user.
        * Tools and Tech: Python3, IBM Cloud Functions, IBM Watson Assitant

   4. **Product Requirements/Scope**
        * One of the important steps in this strategy is documenting product requirements and is focused precisely on shaping a chatbot idea into a working project. I am using **User Stories Framework** to document requirements. The idea behind **high-level user-stories**  is to be in your customer's shoes and that will give a prespective of their expectations from the product, in this case Jarvis. 
        
        **As a** Customer **(who):**
        - **I need** Jarvis to recommend me doctors based on location I provide **(what) so that** I am educated about doctors filtered as per my location preferences **(why)**
        - **I need** Jarvis to have additonal facility to get doctors based on location as well as speciality **(what)so that** I can get results filterd on locaiton and speciality **(why)**

   5. **Prioritize expectations from the chatbot**
        * Since this is a functional demo and we are just asking Jarvis one special task, from a customer point of view, I would expect Jarvis to provide the status of the flight whenever asked. 

   6. **Design a Conversational Design Flow**
        * Chatbots needs to plan their dialog use cases in advance to engage with the user and do not get lost in the conversation. The most important feature is to create a **personality** of the chatbot that is consistent throughout the engagement. Conversational flow is a dialog tree sure every user request is covered by some part of the bot’s logics. 
        
         1. **User Onboarding**  
              - Chatbot should give an introduction along with quick overview of it's abilities
          
         2. **Intents**
              - Intents are used to capture the user's intention behind the conversation. We want Jarvis to handle user-intents related:
                  - **#get_doctors:** This is the main intent for this demo to handle user's intent to get doctor's info
                  - **#talk_to_agent:** This intent will handle requests if user needs to talk to an agent 
                  - **#cancel :** In case user needs to cancel the request
                  - **Chit Chat:** For the purpose of chit-chat, I made 3 more intents. 
                        - **#greetings**
                        - **#goodbyes**
                        - **#Thank You**
         
         3. **Entities**
              - Next as per the use-case we need to create entities that store informaiton from the user related to intents and that provide specific context to intents. IBM Watson Assistant provide system level entities as well that we can enable and the assistant will detect the entities automatically. For this use-case, I used/created following system/entites:
                  - **@sys-location:** System entity that detects and extracts locations/addresses
                  - **@sys-date:** System entity that detects dates for future additional functionality to filter results by
                  - **@sys-person:** System entity that detects and extracts user's name from the input
                  - **@Phone_Number:** Pattern Enitity to extract phone-numbers used with IBM Watson Assitant's advanced feature **Pattern Matching** that enforces phone number to be in format xxx-xxx-xxxx.
                  - **@Speciality:** Additional entity to extend bot's ability to filter results by doctor's specialitites 
         
         4. **Context Variables**
              - Using context variables assitant can pass information to the dialog nodes or even can be used as parameters to communicate with backend services and/or third-party APIs. I created the following context-variables:
                - **agentCounter:** This variable keeps a track of number of times Jarvis is unable to understand the request and gets incremented every time and if the counter > 2, it transfers to an user-agent
                - **my_creds:** This variable just stores the IBM Cloud Functions Namespace credentials
         
         5. **Design the dialog in a optimized way**
            * Dialog Nodes
              - Dialog Node flows in-order, therefore order matters:
                  - Welcome
                  - Get Location-Based Doctor Info
                  - Escalate to an agent
                  - Chit Chat
                  - Anything Else
              
            * Dialog Practices
              - Responses/questions should be precise and straightforward sentences/questions
              - Avoiding open-ended questions
              - Following the natural flow of a conversation
              - Diversify bot's replies whenever possible 
         
         6. **Be consistent with Bot's persona**
              - Use the communication style to stay consistent with the chatbot's personality
         
   7. **Monitor the analytics once deployed to the customers**
         * This is a future step to incorporate, analyzing failure issues and patterns backtracking to imporvising intents, utterances, etc. 
  

### Content
   - [x] Creativity of creating the dialog to develop orignal conversational content
   - _Note: The output is the spoken and not displayed as text on screen. People generally speak differently than how they write_
 
### Intents
   - [x] Optimize the sample intents to capture the most common ways someone may say a certian intent, while using no more than 10 unique intents

### API Integration
   - [x] Syntax, following the Object Oriented Principles, and general convention / best practices of the selected microservice language. 
   - [x] Proper Implementation of RESTful or SOAP API, taking into account a reasonable range of scenarios and parameters. 
   - [x] Implement error handling that produces a user friendly message
   - [x] Transform JSON/XML data to a string that can be spoken in the target human language

### Use of Advanced NLP Features
   - [ ] Proper implementation of at least two of the following advanced NLP features:
          - [ ] Digressions
          - [x] Pattern Entities
          - [x] Slots / Variables
          - [ ] Dual simultaneous Intents / Follow-Up Intents

### Quality Assurance
   - [x] Overall quality of the final corpus and user experience
   - _Note: Generally the measurement for this would be how many unexpected errors or behaviours were encountered_ 

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

1. [BetterDoctor API Documentation](https://developer.betterdoctor.com/documentation15)
2. [IBM's Slots Tutorial](https://www.youtube.com/watch?v=mrHgLCNraf8&feature=youtu.be)
3. [IBM Webhook's Demo by Erika](https://medium.com/ibm-watson/chatting-with-watson-to-hook-any-tweets-webhook-tutorial-bf0fac67d604)
4. [Define chatbot strategy](https://www.digiteum.com/10-steps-to-define-your-chatbot-strategy/)
5. [Document chatbot requirements](https://chatbotsmagazine.com/how-to-document-chatbot-requirements-7df81275cc66)
6. [Conversation Design](https://www.digiteum.com/conversational-ux-7-tips-creating-effective-chatbot-user-experience/)
