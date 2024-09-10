import Card from "./Card";
import { useState, useEffect } from "react";
import Modal from 'react-modal';

Modal.setAppElement('#root');

function App() {
    const [Cards, setCards] = useState([]);
    const [FullName,setFullName] = useState("Friend Name");
    const [Role,setRole] = useState("Unknown");
    const [Description,setDescription] = useState("No Description");

    async function getCards() {
        const response = await fetch("http://127.0.0.1:8888/Cards");
        const response_json = await response.json();
        setCards(response_json);
    }
    

    async function addCard() {
      // First we create a new User
      const response =   await fetch("http://127.0.0.1:8888/create_user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              fullname: FullName,
              role: Role,
            }),
        });
      const response_json = await response.json(); 
     
      // Then we create a new Card
        await fetch("http://127.0.0.1:8888/create_card", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            userid: response_json.userid,
            description: Description,
          }),
      });
      //Update Cards
      getCards();
        
    }

    useEffect(() => {
        getCards();
    }, []);

    const [modalIsOpen, setModalIsOpen] = useState(false);

    const openModal = () => setModalIsOpen(true);
    const closeModal = () => setModalIsOpen(false);

    return (
        <div className="container mx-auto p-4">
            {/* Header */}
            <div className="flex flex-row p-2 justify-start gap-2">
                <h1 className="text-3xl">Friends</h1>
                <button onClick={openModal}>
                    <i className="fa-solid fa-square-plus text-xl"></i>
                </button>
            </div>
            {/* Cards */}
            <div className="flex flex-wrap items-center justify-center">
               {Cards.map((card) => (
                    <Card
                        key={card.Cardid}
                        FullName={card.Userinfo.FullName}
                        Role={card.Userinfo.Role}
                        Description={card.Description}
                        GetCards = {getCards}
                        CardId = {card.Cardid}
                    />
               ))}
            </div>
            {/* Dialog */}
            <Modal
                isOpen={modalIsOpen}
                onRequestClose={closeModal}
                className="bg-primrary p-2 rounded-lg w-[450px] border-[1px] border-blue-500"
                overlayClassName="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center"
            >
                <div className="flex flex-col gap-2">
                  <h1 className="text-xl">New Card</h1>
                  <div className="flex flex-row ml-5 gap-32">
                    <span>Full name</span>
                    <span>Role</span>

                  </div>
                  <div className="flex flex-row gap-3 items-center justify-center">
                    <input onChange={(e) => setFullName(e.target.value)} placeholder="John Doe" className="rounded-md text-primrary pl-3" type="text" />
                    <input onChange={(e) => setRole(e.target.value)} placeholder="Developer/AI Engineer..." className="rounded-md text-primrary pl-3" type="text" />
                  </div>
                  <div className="flex flex-col gap-1 ml-2 mr-2 mb-2">
                      <span>Description</span>
                      <input onChange={(e) => setDescription(e.target.value)} placeholder="Nouredine is ..." className="rounded-md text-primrary pl-3" type="text" />
                  </div>
                  <div className="flex flex-row gap-3 justify-end m-3">
                    <button onClick={()=>{addCard();closeModal()}} className="rounded-md border-2 p-1 text-blue">Submit</button>
                    <button onClick={closeModal} className="rounded-md border-2 p-1 text-red">Cancel</button>
                  </div>

                </div>
            </Modal>
        </div>
    );
}

export default App;
