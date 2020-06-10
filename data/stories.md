## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path + faq
* greet
    - utter_greet
* ask_faq
    - respond_ask_faq
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Some question from FAQ
* ask_faq
    - respond_ask_faq



## happy path
* greet 
	- utter_greet 
* request_restaurant 
	- restaurant_form 
	- form{"name": "restaurant_form"} 
	- form{"name": null} 
	- utter_slots_values
* thankyou
	- utter_noworries 