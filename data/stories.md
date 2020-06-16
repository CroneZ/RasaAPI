## pick_up_delivery
* deliver_parcel
    - pick_up_form
    - form{ "name" : "pick_up_form" }<!--Activate Form-->
    - form{ "name" : null }

## parcel_inquiry
* parcel_inquiry
    - inquire_form
    - form{ "name" : "inquire_form" } <!--Activate Form-->
    - form{ "name" : null } <!--Deactivate Form-->


## interactive_story_1
* deliver_parcel
    - pick_up_form
    - form{"name": "pick_up_form"}
    - slot{"requested_slot": "address"}
* form: inform{"address": "NO 20, JALAN 20C/146 , DESA TASIK"}
    - slot{"address": "NO 20, JALAN 20C/146 , DESA TASIK"}
    - form: pick_up_form
    - slot{"address": "NO 20, JALAN 20C/146 , DESA TASIK"}
    - slot{"requested_slot": "address2"}
* form: inform{"address2": "NO 48,JALAN MH4/2, AYER KEROH"}
    - slot{"address2": "NO 48,JALAN MH4/2, AYER KEROH"}
    - form: pick_up_form
    - slot{"address2": "NO 48,JALAN MH4/2, AYER KEROH"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}
* parcel_inquiry
    - inquire_form
    - form{"name": "inquire_form"}
    - slot{"requested_slot": "tracking_id"}
* form: inform{"tracking_id": "JJD0116767890"}
    - slot{"tracking_id": "JJD0116767890"}
    - form: inquire_form
    - slot{"tracking_id": "JJD0116767890"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_deactivate_form
    - form{"name": null}
    - slot{"requested_slot": null}

## Frequently_asked
* faq
    - respond_faq