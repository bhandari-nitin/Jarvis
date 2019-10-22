# Jarvis - The ChatBot

## Introduction 
> This is a conversational bot using IBM Watson API for <project> integrated with slack and uses [**Flightware API**](https://flightaware.com/commercial/flightxml/) to check on the status of a flight. 

### Documentaion
- [Ideation and Scoping](#ideation-and-scoping)
- [Content ](#content)
- [Intents](#intents)
- [API Integration](#api-integration)
- [Use of Advanced NLP Features](#use-of-advanced-nlp-features)
- [Quality Assurance](#quality-assurance)

#### Ideation and Scoping (20 pts)
  - [x] Documentation of ideation, content, and functionality
  - [ ] Documentaion of Scope in format of User Stories/other format of your choice
  
  Turning a chatbot idea requires a complete step-by-step chatbot strategy from goal defination to publishing and maintainence. 
  
   1. **Defining Goals**\
        Jarvis will connect to Flightware API to check on the status of a flight. Creating a chatbot there are many things to     define before starting

   2. **Understand Users**\
        `Assumption:` The users of this bot are people who like to go on holidays and people who fly frequently, so they might ask Jarvis to check the status of their flight. 

   3. **Tools**\
        Jarvis uses [Flightaware API](https://flightaware.com/commercial/flightxml/) to fetch the status of the flights once the user provides the flight details. 

   4. **Product Requirements**\
        One of the important steps in this strategy is documenting product requirements and is focused precisely on shaping a chatbot idea into a working project. I am using **User Stories Framework** to document requirements.The idea behind is to be in your customer's shoes and that will give a prespective of their expectations from the product, in this case Jarvis. 
        
        **As a** Customer 
        - **I need** Jarvis to provide me the status of a flight **so that** I can be at airport on time. 
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**
        
        **As a** Customer Facing Engineer 
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**
        
        **As a** Support Manager 
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**
        - **I need** blah blah **so that**


   5. **Prioritize expectations from the chatbot**\
        Since this is a functional demo and we are just asking Jarvis one special task, from a customer point of view, I would expect Jarvis to provide the status of the flight whenever asked. 

   6. **Design a Conversational Flow**\
        Chatbots needs to plan their dialog use cases in advance to engage with the user and do not get lost in the conversation. The most important feature is to create a **personality** of the chatbot that is consistent throughout the engagement. 
        
         1. User Onboarding\ 
          - Chatbot should give an introduction along with quick overview of it's abilities
          
         2. Minimize user effort\
         - To minimize user effort, we need to design the conversational flows to get most information from the user in an efficient way
         
         3. Confirm Understanding\
         - Keeping user informed at each step of the conversation is crucial to prevent any ambiguity. 
         
         4. Design the dialog in a optimized way\
         - Responses/questions should be precise and straightforward sentences/questions
         - Avoiding open-ended questions
         - Following the natural flow of a conversation
         - Diversify bot's replies whenever possible 
         
         5. Be consistent with Bot's persona\
         - Use the communication style to stay consistent with the chatbot's personality
         
         6. Provide visual clues\
         - It's a good idea to add visual cards when explaining the difference between several things or products
       

   7. **Monitor the analytics once deployed to the customers**\
        This is a future step to incorporate, analyzing failure issues and patterns backtracking to imporvising intents, utterances, etc. 
  

#### Content (20 pts)
  - [ ] Creativity of creating the dialog to develop orignal conversational content
  - _Note: The output is the spoken and not displayed as text on screen. People generally speak differently than how they write_
 
#### Intents (20 pts)
  - [ ] Optimize the sample intents to capture the most common ways someone may say a certian intent, while using **no more than 10 unique intents**

#### API Integration (20 pts)
  - [ ] Syntax, following the Object Oriented Principles, and general convention / best practices of the selected microservice language. 
  - [ ] Proper Implementation of RESTful or SOAP API, taking into account a reasonable range of scenarios and parameters. 
  - [ ] Implement error handling that produces a user friendly message
  - [ ] Transform JSON/XML data to a string that can be spoken in the target human language

#### Use of Advanced NLP Features (10 pts)
  - [ ] Proper implementation of at least two of the following advanced NLP features:
       - [ ] Digressions
       - [ ] Pattern Entities
       - [ ] Slots / Variables
       - [ ] Dual simultaneous Intents / Follow-Up Intents

#### Quality Assurance (10 pts)
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
