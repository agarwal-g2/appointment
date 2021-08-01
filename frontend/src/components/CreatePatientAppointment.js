import React, { useState, useEffect } from "react";
import { API_BASE_URL } from "../App";
import axios from "axios";

const getPatient = async () => {
  try {
    const result = await axios.get(API_BASE_URL + "/patients/");
    return result.data;
  } catch (e) {
    console.error(e);
    return null;
  }
};

const createPatientAppointment = async (patientId, appointmentId) => {
  try {
    const result = await axios.patch(API_BASE_URL + "/appointments/"+appointmentId.target.value+"/book/", {
      patient_pk: patientId.target.value
    });
    return result.data;
  } catch (e) {
    console.error(e);
    return e.response.data ? e.response.data :"Unable to create patient appointment"
  }
};

const CreatePatientAppointment = ( {appointments} ) => {
  let [patientId, setPatientId] = useState();
  let [appointmentId, setAppointmentId] = useState();

  const [patientList, setPatientList] = useState()
  const [appointmentList, setAppointmentList] = useState()
  const [isLoading, setIsLoading] = useState(false);
  const [submitMessage, setSubmitMessage] = useState("");

  useEffect(() => {
    getPatient().then(res => {
      setPatientList(res.map(r => ({value: r.pk, label : (r.first_name + " " + r.last_name)})))
    })

  }, [])

  useEffect(() => {
    const appointmentList = appointments.map(a => {
      return {
        value: a.pk, label : (a.start_time)
      }
    });
    setAppointmentList(appointmentList)

  }, [appointments])

  const handleSubmit = async (event) => {
    event.preventDefault();
    setSubmitMessage("");
    setPatientId = (event) => this.setState({patientId : event.target[0].value});
    setAppointmentId = (event) => this.setState({appointmentId : event.target[1].value})

    const result = await createPatientAppointment(patientId, appointmentId);

    setSubmitMessage(JSON.stringify(result));
    setIsLoading(false);
  };

  return (
    <>
      <h2>Book appointment for patient</h2>
      <form onSubmit={handleSubmit}>
        <label >Patient Name:</label><br/>
        { patientList &&
          <select
            onChange={setPatientId}
          >
            {patientList.map((option) => (
              <option value={option.value}>{option.label}</option>
            ))}
          </select>
        }<br/>
      <label >Appointment Start:</label><br/>
        { appointmentList &&
          <select
            onChange={setAppointmentId}
          >
            {appointmentList.map((option) => (
              <option value={option.value}>{option.label}</option>
            ))}
          </select>
        }
        <br/>
        <button type="submit" disabled={isLoading}>
          Submit
        </button>
      </form>
      {submitMessage && (
        <p>
          <i>{submitMessage}</i>
        </p>
      )}
    </>
  );
}



export default CreatePatientAppointment