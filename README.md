#Approach 

There were two main approaches to attempt this assignment

- First to link paitientId inside the appointment model and store it But the problem with this approach was we already had a patch request which was accepting appointment id, so it was not possible to pass the appointment id at the time of creation unless we need to create another post API for the same. But then the user experience will be bad as we first need to create an appointment and then map it with the patient id. And since I need to fix it in the existing code base so I didn’t choose this approach.

- The second approach was to take the existing appointment as a slot and link that slot with the patient(and practitioner in the future) in the new patientAppointment table. This approach is more scalable as we can make slots free/booked/canceled in the future without changing the main slot.

#Future Improvements
- Add patient unique identifier like email/phone so that while booking slot there won’t be duplicate name’s
- Add validations for the appointment creation like
  - The end date should be greater than the start
  - An appointment should not be created if an appointment already exists in the time interval
  - Patient creation field validation
- The list should show the newly created data without refresh
- We can add a practitioner as well in the booking table to identify the participants 
- When we delete a
  - Patient: then first we need to change the status of all the scheduled appointments to cancel, then mark all those slots available, and then mark the patient as soft deleted.
  - Appointment: In case of deleting the appointment, just change the status to canceled and make those slots available for another booking. Also, trigger notifications to participants.

