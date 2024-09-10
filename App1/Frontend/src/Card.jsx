


function Card({ FullName, Description,Role,GetCards,CardId }) 
{
    async function DropCard()
    {
        

        const options =
        {
            method: "DELETE",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                cardid: CardId
            }),
        }
        await fetch("http://127.0.0.1:8888/delete_card", options);
        GetCards();
        
    }

    return (
        <div className="flex flex-col w-[400px] h-[200px] border-none rounded-md p-5
         m-5 bg-white gap-16">
            {/* Header of the Card */}
            <div className="flex flex-row justify-between">
                <div>
                    <h3 className="text-xl">{FullName}</h3>
                    <h4 className="text-sm">{Role}</h4>
                </div>
                <div>
                    <button className="m-2 text-xl text-red"
                    onClick={()=>{DropCard();console.log(CardId);}}>
                    <i className="fa-solid fa-trash"></i>
                    </button>
                    <button className="text-xl text-blue-500">
                    <i className="fa-solid fa-pen-to-square"></i>
                    </button>
                </div>
            </div>
            {/* Description */}
            <p className="">{Description}</p>
        </div>
    );
}

export default Card;
