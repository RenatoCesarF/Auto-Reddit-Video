
import {TbArrowBigTop, TbArrowBigDown} from "react-icons/tb"

type flexDirectionType = "row" | "column";

interface VoteBarInterface{ 
    amount: number, 
    flexDirection?: flexDirectionType
}
const VoteBar = ({amount, flexDirection = 'column'}: VoteBarInterface) =>{

    return(
        <div className={'vote-bar-wrapper'} style={{"flexDirection": flexDirection}}> 
            <TbArrowBigTop  size={50} className="hightlight"/>
            <span style={{fontSize: "25px"}}>{amount}</span>
            <TbArrowBigDown size={50} style={{color: "#818384"}}/>
        </div>
    )
}

export default VoteBar