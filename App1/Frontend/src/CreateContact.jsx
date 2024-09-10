
import  {useState} from 'react'

function CreateContact(args) {
    const [FirstName, setFirstName] = useState('')
    const [LastName, setLastName] = useState('')
    const [IsStudent, setIsStudent] = useState(false)
    const [Email, setEmail] = useState('')


    async function AddContact(){
        const data = {
            "firstName": FirstName,
            "lastName": LastName,
            "isStudent": IsStudent,
            "email": Email
        }
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Tell backend that we are sending JSON
            },
            body: JSON.stringify(data)
        }
        const response = await fetch('http://localhost:5000/create', options)
        const json = await response.json()
        //alert(json.message)
        args.getData()
    }

    return(
         <div className='p-4 flex flex-col items-start border-2 m-5 rounded-md'>
            <div className='flex flex-row p-2'>
                <h3 className='font-semibold'>First Name : </h3>
                <input className='border-2 ml-2' type="text" onChange={(e)=>setFirstName(e.target.value)}/>
            </div>

            <div className='flex flex-row p-2'>
                <h3 className='font-semibold'>Last Name : </h3>
                <input className='border-2 ml-2' type="text" onChange={(e)=>setLastName(e.target.value)}/>
            </div>
            
            <div className='flex flex-row p-2'>
                <h3 className='font-semibold'>Email : </h3>
                <input className='border-2 ml-12' type="text" onChange={(e)=>setEmail(e.target.value)}/>
            </div>
            
            <div className='flex flex-row p-2'>
                <h3 className='font-semibold'>Is Student  ? </h3>
                <input className='border-2 ml-2 ' type="checkbox" onChange={(e)=>setIsStudent(e.target.checked)}/>
            </div>
             
            <button className='border-2 p-1 font-semibold ml-[50%]' onClick={AddContact}>Create</button>
         </div>
    )

}

export default CreateContact
