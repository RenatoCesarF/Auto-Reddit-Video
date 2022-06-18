
import {TbArrowBigTop, TbArrowBigDown} from "react-icons/tb"

type flexDirectionType = "row" | "column";

interface VoteBarInterface{ 
    amount: number, 
    flexDirection?: flexDirectionType,
    iconSize?: number
}
const VoteBar = ({amount, flexDirection = 'column', iconSize = 50}: VoteBarInterface) =>{

    return(
        <div className='vote-bar-wrapper' style={{flexDirection: flexDirection}}> 
            <TbArrowBigTop  size={iconSize} className="hightlight"/>
            <span style={{fontSize: "25px"}}>{amount}</span>
            <TbArrowBigDown size={iconSize} style={{color: "#818384"}}/>
        </div>
    )
}

export default VoteBar