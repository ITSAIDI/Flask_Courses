function ContactsList(props) {  
    const {contacts,getData} = props;
    async function DeleteContact(id){
        const options = {
            method: 'DELETE',
        }
        const response = await fetch(`http://localhost:5000/delete/${id}`,options)
        const json = await response.json()
        //alert(json.message)
        getData()
    }
    
    return (
       <div>
        <h2 className="p-5">Contacts</h2>
        <table className="ml-5 border-2">
            <thead className="border-2">
                <tr className="">
                    <th className="p-2 border-2">Id</th>
                    <th className="p-2 border-2 ">FirstName</th>
                    <th className="p-2 border-2">LastName</th>   
                    <th className="p-2 border-2">IsStudent</th>
                    <th className="p-2 border-2">Email</th>
                    <th className="p-2 border-2">Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map((contact) => (
                    <tr 
                    className="odd:bg-white even:bg-slate-100"
                    key={contact.id}>
                        <td>{contact.id}</td>
                        <td>{contact.firstName}</td>
                        <td>{contact.lastName}</td>
                        <td>{contact.isStudent}</td>
                        <td>{contact.email}</td>
                        <td>
                            <button className="border-2 rounded-md text-green-400 border-green-500 m-2 p-1">Edit</button>
                            <button className="border-2 rounded-md text-red-400 border-red-500 p-1" onClick={() => DeleteContact(contact.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
       </div>
    );
}

export default ContactsList;
