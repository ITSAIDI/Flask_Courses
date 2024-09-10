import { useState,useEffect } from "react"
import ContactsList from "./ContactsList"
import CreateContact from "./CreateContact"

function App() {

  const [Contacts,setContacts]= useState([])
  useEffect(()=>{getData()},[])

  function Simplemap(data)
  {
    return (
      data.map((contact)=>({
        "id": contact[0],
        "firstName": contact[1],
        "lastName": contact[2],
        "isStudent": contact[3],
        "email": contact[4]
      }))
    )
  }


  async function getData(){
    const response = await fetch("http://127.0.0.1:5000/contacts")
    let data = await response.json()
    //console.log(data)
    data = Simplemap(data.contacts)
    setContacts(data)
  }
  
  return (
    <div className="App">
      <ContactsList contacts = {Contacts} getData={getData}></ContactsList>
      <CreateContact  getData={getData}></CreateContact>

    </div>
  )
}

export default App
