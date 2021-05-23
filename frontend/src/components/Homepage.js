import React, { createRef, useState, useCallback } from "react";
import {FightInput} from './FightInput.js'
import {Winner} from './Winner.js'
import { Redirect } from "react-router";
function Homepage(props){
    let [winner, setWinner] = useState(null)
    let [redirect, setRedirect] = useState(null)
    // document.body.style = 'background:rgba(129,102,13,.5)'
    if (redirect != null){
        const redirect = "/components/about"
        return <Redirect push to = {redirect}/>
    }
    return (
        <div style = {{
            background:'linear-gradient(to right, rgba(196,196,196,.9), rgba(234,234,234,.9))',
            height:"100vh",
            fontFamily:'Kanit'
        }}>
            <div>
                <h1 style = {{
                    textAlign:'center',
                    fontSize:"75pt",
                    color: 'gray',
                    textShadow:"2px 2px 2px black",
                    marginBottom:'100px',
                }}>UFC JUDGE</h1>
                <FightInput setWinner={setWinner}/>
                <Winner win = {winner} />
                
            </div>
            <div 
                style = {{
                    position:'fixed',
                    height:"10px",
                    width:"20px",
                    bottom:"20",
                    fontSize:'20pt',
                    cursor:'pointer'}}
                onMouseDown={()=>{
                    
                    setRedirect(true)
                    }} >
                <p>About</p>
            </div>
        </div>

    )

}

export {Homepage}