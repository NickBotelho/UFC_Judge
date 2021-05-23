import React, { createRef, useState, useCallback } from "react";
import {Homepage} from './Homepage.js'
import {Routing} from '../routing.js'
function App(props){
    let [winner, setWinner] = useState(null)
    // document.body.style = 'background:rgba(129,102,13,.5)'
    return (
        <div style = {{
            background:'linear-gradient(to right, rgba(196,196,196,.9), rgba(234,234,234,.9))',
            height:"100vh",
            fontFamily:'Kanit'
        }}>
            <Routing/>
        </div>

    )

}

export {App}